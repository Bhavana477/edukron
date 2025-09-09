import numpy as np
import pandas as pd

def optimize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimize numeric dtypes:
    
      - Integers → int8 / int16 / int32
      - Floats   → float16 / float32
    Returns a DataFrame with reduced memory usage.
    """
    before = df.memory_usage(deep=True).sum() / 1024**2
    optimized = df.copy()

    for col in optimized.columns:
        s = optimized[col]

        # --- Integers ---
        if pd.api.types.is_integer_dtype(s):
            vals = s.astype("int64")  # safe for bound checks
            if vals.min() >= np.iinfo(np.int8).min and vals.max() <= np.iinfo(np.int8).max:
                optimized[col] = s.astype("int8")
            elif vals.min() >= np.iinfo(np.int16).min and vals.max() <= np.iinfo(np.int16).max:
                optimized[col] = s.astype("int16")
            elif vals.min() >= np.iinfo(np.int32).min and vals.max() <= np.iinfo(np.int32).max:
                optimized[col] = s.astype("int32")
            # else: leave unchanged if too large

        # --- Floats ---
        elif pd.api.types.is_float_dtype(s):
            s64 = s.astype("float64")
            if np.allclose(s64, s64.astype("float16"), rtol=1e-03, atol=1e-06, equal_nan=True):
                optimized[col] = s64.astype("float16")
            else:
                optimized[col] = s64.astype("float32")

    after = optimized.memory_usage(deep=True).sum() / 1024**2
    print(f"Memory: {before:.3f} MB → {after:.3f} MB ({(before - after) / before * 100:.2f}% reduction)")

    return optimized.shape

