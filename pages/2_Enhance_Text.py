import streamlit as st

from core.middlewares import openai_required_middleware
from core.ui.sidebar import sidebar
from core.utils import count_words, get_enhanced_text, get_my_current_text_level

# A Middleware-like for checking OpenAI key
openai_required_middleware()

# Sidebar
sidebar()


st.write("# Enhance Text")
text: str = st.text_area("**My Text:**")

words = count_words(text)
st.write(f"*Worlds: {words}*")

col1, col2 = st.columns(2)

with col1:
    enhance = st.button("🔁 Enhance My Text!", use_container_width=True)

with col2:
    my_level = st.button("✨ Detect My Current Text Level?", use_container_width=True)

with st.spinner("Running..."):
    if text:
        if enhance:
            st.write(f"### Enhanced Text (Level: {st.session_state.english_level}):")
            st.write(get_enhanced_text(text))

        if my_level:
            st.write("### My Current Text Level:")
            st.write(get_my_current_text_level(text))
    else:
        st.warning("Please write someting.")
