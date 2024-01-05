import streamlit as st

st.write("# Settings")

tab1, tab2, tab3 = st.tabs(["**General**", "**OpenAI settings**", "**SMTP**"])

with tab1:
	st.write("General Settings")

with tab2:
	st.write("OpenAI Settings")

with tab3:
	st.write("SMTP Settings")
