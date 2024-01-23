import streamlit as st

from core.middlewares import openai_required_middleware
from core.ui.sidebar import sidebar
from core.utils import get_text_answer

# A Middleware-like for checking OpenAI key
openai_required_middleware()

# Sidebar
sidebar()

st.write("# Text Comprehension")

text: str = st.text_area("**Text:**")
question: str = st.text_area("**Question:**")
submit = st.button("✨ Answer", use_container_width=True)

if submit:
    with st.spinner("Running..."):
        st.write(get_text_answer(text, question))
