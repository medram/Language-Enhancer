import streamlit as st

from streamlit_extras.switch_page_button import switch_page

from core.utils import is_api_key_valid


st.info("⚠️ OpenAI key is required before starting using the app *(put a key and hit enter)*.")
key = st.text_input("**OpenAI key:**", type="password", placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxxxx")

if key:
	if is_api_key_valid(key):
		st.session_state.openai_key = key
		switch_page("app")
	else:
		st.warning("⚠️ Invalid OpenAI key!")

