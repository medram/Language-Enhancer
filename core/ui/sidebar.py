from typing import Optional

import streamlit as st

from core.middlewares import openai_required_middleware
from core.utils import AVAILABLE_AI_MODELS, LANGUAGE_LEVELS, get_current_model_by_name

# A Middleware-like for checking OpenAI key
openai_required_middleware()


def sidebar():
    # Sidebar
    with st.sidebar:
        st.write("## Settings")
        st.session_state.english_level = st.selectbox(
            "**English Level:**", LANGUAGE_LEVELS, index=4
        )

        st.divider()
        st.write("## OpenAI settings")

        selected_model_name = str(
            st.selectbox("**Model:**", AVAILABLE_AI_MODELS, index=0)
        )

        st.session_state.temp = st.slider(
            "Temperature:", min_value=0.0, max_value=2.0, value=0.5
        )

        current_model = get_current_model_by_name(selected_model_name)

        st.session_state.max_tokens = st.slider(
            "Max Tokens:", min_value=1, max_value=current_model.max_tokens, value=1024
        )
