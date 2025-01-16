import streamlit as st
from app.constants.agriculture_school_constants import agri_school_content
from app.utils.suprise_me_util import get_surprise_content


def agriculture_school(selected_language):
    # Gets the data for the selected language
    st.markdown(
        """
    <style>
    .stButton button {
        transition: all 0.2s;
        border: 1px solid #8ac774;
        color: #8ac774;
        font-weight: 500;
        padding: 8px 16px;
        border-radius: 6px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }


</style>
    """,
        unsafe_allow_html=True,
    )
    st.image("static/farmer_learning.jpg")
    lang_content = agri_school_content[selected_language]

    st.header(lang_content["title"])
    user_question = st.chat_input(lang_content["input_placeholder"])
    if user_question:
        return
    # --- Surprise Me Button ---
    if st.button(lang_content["surprise_me_button"]):
        educational_content = get_surprise_content(lang_content)
        if not educational_content["heading"] or not educational_content["content"]:
            st.error("Error fetching content. Please try again later.")
            return
        st.header(educational_content["heading"], anchor=None)
        st.write(educational_content["content"])

    return
