import streamlit as st
from constants.agriculture_school_constants import agri_school_content
import random
import time


def agriculture_school(selected_language):
    # Gets the data for the selected language
    st.image("static/farmer_learning.jpg")
    lang_content = agri_school_content[selected_language]

    st.header(lang_content["title"])
    user_question = st.chat_input(lang_content["input_placeholder"])
    if user_question:
        return
    # --- Surprise Me Button ---
    if st.button(lang_content["surprise_me_button"]):
        random_topic = random.choice(list(lang_content["topics"].keys()))
        st.write(lang_content["surprise_me_text"].format(random_topic))
        st.write(lang_content["topics"][random_topic])

    return
