import streamlit as st
from components.sidebar import streamlit_sidebar
from components.agriculture_school import agriculture_school


def main():
    # --- Page Configuration ---
    st.set_page_config(
        page_title="Kisan Sahayak",
        page_icon="🌾",
        layout="wide",
    )

    [selected_feature_id, selected_language] = streamlit_sidebar()

    if selected_feature_id == "krishi_pathshala":
        agriculture_school(selected_language)


if __name__ == "__main__":
    main()
