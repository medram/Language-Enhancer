import streamlit as st
from streamlit_extras.switch_page_button import switch_page


def openai_required_middleware():
    if "openai_key" not in st.session_state:
        switch_page("app")
