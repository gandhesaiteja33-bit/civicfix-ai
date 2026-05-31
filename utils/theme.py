import streamlit as st


def apply_theme():

    theme = st.sidebar.selectbox(
        "🎨 Theme",
        ["Light", "Dark"]
    )

    if theme == "Dark":

        st.markdown("""
        <style>

        .stApp {
            background-color:#0E1117;
            color:white;
        }

        .block-container {
            padding-top:1rem;
        }

        </style>
        """,
        unsafe_allow_html=True)

    return theme