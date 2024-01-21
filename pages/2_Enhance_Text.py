import streamlit as st

from core.middlewares import openai_required_middleware
from core.ui.sidebar import sidebar

# A Middleware-like for checking OpenAI key
openai_required_middleware()

# Sidebar
sidebar()


st.write("# Enhance Text")
st.text_area("**My Text:**")


col1, col2 = st.columns(2)

with col1:
    enhance = st.button("🔁 Enhance My Text!", use_container_width=True)
with col2:
    my_level = st.button("✨ Detect My Current Text Level?", use_container_width=True)

if enhance:
    st.write(f"### Enhanced Text (Level: {st.session_state.english_level}):")

if my_level:
    st.write("### My Current Text Level:")
