import streamlit as st

from core.sidebar import sidebar

# Sidebar
sidebar()


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
