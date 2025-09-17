import streamlit as st

def apply_global_filters(df):
    st.sidebar.header("🔍 Global Filters")


    # --- Gender ---
    gender = st.sidebar.multiselect(
        "Gender",
        df["CODE_GENDER"].dropna().unique().tolist(),
        default=df["CODE_GENDER"].dropna().unique().tolist()
    )

    # --- Education ---
    education = st.sidebar.multiselect(
        "Education",
        df["NAME_EDUCATION_TYPE"].dropna().unique().tolist(),
        default=df["NAME_EDUCATION_TYPE"].dropna().unique().tolist()
    )

    # --- Family Status ---
    family_status = st.sidebar.multiselect(
        "Family Status",
        df["NAME_FAMILY_STATUS"].dropna().unique().tolist(),
        default=df["NAME_FAMILY_STATUS"].dropna().unique().tolist()
    )

    # --- Housing Type ---
    housing = st.sidebar.multiselect(
        "Housing Type",
        df["NAME_HOUSING_TYPE"].dropna().unique().tolist(),
        default=df["NAME_HOUSING_TYPE"].dropna().unique().tolist()
    )
