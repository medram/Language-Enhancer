import streamlit as st

from core.middlewares import openai_required_middleware
from core.utils import LANGUAGE_LEVELS, AVAILABLE_AI_MODELS

# A Middleware-like for checking OpenAI key
openai_required_middleware()


with st.sidebar:
	st.write("## Settings")
	st.selectbox("**English Level:**", LANGUAGE_LEVELS, index=4)

	st.divider()
	st.write("## OpenAI settings")

	st.selectbox("**Model:**", AVAILABLE_AI_MODELS)
	st.session_state.temp = st.slider("Temperature:", min_value=0.0, max_value=2.0, value=0.5)
	st.session_state.max_tokens = st.slider("Max Tokens:", min_value=10, max_value=4096, value=1024)


st.write("# Text Comprehension")

text = st.text_area("**Text:**")
question = st.text_area("**Question:**")
submit = st.button("Submit", use_container_width=True)

if submit:
	st.write("Nice :D")


"""
OpenAI key, temperature, model

functionality:
- Text comprehension (Answer Questions)
	- Text input
	- Text Question
- English level & give an enhanced version
	- Text input
"""


