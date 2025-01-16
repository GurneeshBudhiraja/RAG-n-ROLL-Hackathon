import streamlit as st
from app.constants.sidebar_constants import (
    supported_languages,
    features_dict,
    footer_content,
)


def streamlit_sidebar():
    # Logo
    st.logo("static/logo.jpeg", size="large", icon_image="static/logo.jpeg")

    # Language selection option
    selected_language = st.sidebar.selectbox("Select Language", supported_languages)

    # --- Navigation ---
    # Gets all the features of the selected language
    features = [feat["feat_name"] for feat in features_dict[selected_language]]

    # Store the selected feature ID in session state. Defaults to the first feature
    if "selected_feature_id" not in st.session_state:
        st.session_state.selected_feature_id = features_dict[selected_language][0][
            "feat_id"
        ]

    # Get the currently selected feature name based on the ID
    current_feature_name = next(
        (
            item["feat_name"]
            for item in features_dict[selected_language]
            if item["feat_id"] == st.session_state.selected_feature_id
        ),
        features[0],  # Fallback to the first feature name if not found
    )

    # Display the features in the sidebar (using selectbox)
    selected_feature_name = st.sidebar.selectbox(
        "How can we help you today?",
        features,
        index=features.index(current_feature_name),
    )

    # Update the selected feature ID in session state
    st.session_state.selected_feature_id = next(
        (
            item["feat_id"]
            for item in features_dict[selected_language]
            if item["feat_name"] == selected_feature_name
        ),
        features_dict[selected_language][0][
            "feat_id"
        ],  # Fallback to the first feature ID
    )

    # --- Footer ---
    st.sidebar.markdown(footer_content[selected_language])
    return [st.session_state.selected_feature_id, selected_language]
