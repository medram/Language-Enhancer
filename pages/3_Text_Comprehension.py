from typing import Optional

import streamlit as st

from core.middlewares import openai_required_middleware
from core.ui.sidebar import sidebar

# A Middleware-like for checking OpenAI key
openai_required_middleware()

# Sidebar
sidebar()

st.write("# Text Comprehension")

text = st.text_area("**Text:**")
question = st.text_area("**Question:**")
submit = st.button("Answer", use_container_width=True)

if submit:
    st.write("Nice :D")
