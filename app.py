import time

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="My App", page_icon=":shark:")


if "level" not in st.session_state:
    st.session_state.level = 50


with st.sidebar:
    st.write("# Advanced Settings")

    level = st.slider("**Level:**", min_value=1, value=50)
    st.session_state.level = level
    st.write(f"Current level: **{level}**")

    if st.checkbox("Show Data"):
        st.write("Here is the data :D")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
    )
    if gender:
        st.write(f"You're a **{gender}**")


st.write("# Hello Streamlit World!")

col1, col2, col3 = st.columns(3)

col1.metric("**Revenue**", "$25", 4)
col2.metric("**Clicks**", 6545, 12)
col3.metric("**Users**", 187, 8)

st.write(f"Current Level: {st.session_state.level}")


@st.cache_data
def load_data(level: int):
    return (pd.DataFrame(np.random.randn(level, 3), columns=["a", "b", "c"]) + 2) * 100


df = load_data(st.session_state.level)
st.line_chart(df)

key = st.text_input(
    "OpenAI Key:",
    key="key",
    type="password",
    placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxxxx",
)

st.header("This is a header!")

st.color_picker("Color", "#FFFFFF")

st.divider()
