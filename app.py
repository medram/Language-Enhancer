import streamlit as st
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page

from core.utils import is_api_key_valid

col1, _ = st.columns(2)

with col1:
    st.info(
        "⚠️ OpenAI key is required before starting using the app *(put a key and hit enter)*."
    )

    key = st.text_input(
        "**OpenAI key:**", type="password", placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxxxx"
    )
    submit = st.button("🗝️ Use My Key", use_container_width=True)

    if key and submit:
        if is_api_key_valid(key):
            st.session_state.openai_key = key
            st.success("✅ Now you can use the app.")
            # switch_page("app")
        else:
            st.warning("⚠️ Invalid OpenAI key!")
