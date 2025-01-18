import streamlit as st
import app.components.agriculture_school
import app.components.information_access
from app.components.sidebar import streamlit_sidebar
import app.components
from snowflake.snowpark.context import get_active_session




def main():
    # --- Page Configuration ---
    st.set_page_config(
        page_title="Kisan Sahayak",
        page_icon="🌾",
        layout="wide",
    )

    [selected_feature_id, selected_language] = streamlit_sidebar()

    if selected_feature_id == "krishi_pathshala":
        app.components.agriculture_school.agriculture_school(selected_language)
    if selected_feature_id == "scheme_support":
        app.components.information_access.information_access(selected_language)


if __name__ == "__main__":
    main()
