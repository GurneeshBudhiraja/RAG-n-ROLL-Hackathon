import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.core import Root
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

    lang_content = agri_school_content[selected_language]

    st.image("static/farmer_learning.jpg")
    st.header(lang_content["title"])

    st.write(lang_content["description"])  # Add the description back in

    user_question = st.chat_input(lang_content["input_placeholder"])

    # --- Surprise Me Button ---
    if st.button(lang_content["surprise_me_button"]):
        educational_content = get_surprise_content(lang_content)
        if not educational_content["heading"] or not educational_content["content"]:
            st.error("Error fetching content. Please try again later.")
            return
        st.markdown(f"#### {educational_content['heading'].strip()}")
        st.markdown(f"###### {educational_content['content'].strip()}")

    # --- Topic Selection ---
    st.markdown("##### Or select a topic to learn about:")
    selected_topic = st.selectbox(
        "Select the topic",
        lang_content["education_options"],
        index=None,
        placeholder="Choose a topic...",
    )

    if user_question:

        if user_question:
            st.markdown(f"**User asked:**\n{user_question}")
        else:
            st.error("No context found for the given query.")

    return
