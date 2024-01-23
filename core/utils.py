import re
from typing import Optional

import openai
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from streamlit_extras.switch_page_button import switch_page

from core.schemas import OpenAIModel

LANGUAGE_LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]


_AVAILABLE_AI_MODELS = [
    {"name": "gpt-4", "max_tokens": 8191, "is_chat_model": True},
    {"name": "gpt-4-0314", "max_tokens": 8191, "is_chat_model": True},
    {"name": "gpt-4-0613", "max_tokens": 8191, "is_chat_model": True},
    {"name": "gpt-4-1106-preview", "max_tokens": 8191, "is_chat_model": True},
    {"name": "gpt-3.5-turbo", "max_tokens": 4096, "is_chat_model": True},
    {"name": "gpt-3.5-turbo-0301", "max_tokens": 4096, "is_chat_model": True},
    {"name": "gpt-3.5-turbo-0613", "max_tokens": 4096, "is_chat_model": True},
    {"name": "gpt-3.5-turbo-1106", "max_tokens": 4096, "is_chat_model": True},
    {"name": "gpt-3.5-turbo-16k", "max_tokens": 16384, "is_chat_model": True},
    {"name": "gpt-3.5-turbo-16k-0613", "max_tokens": 16384, "is_chat_model": True},
]

AVAILABLE_AI_MODELS: list[OpenAIModel] = [
    OpenAIModel.model_validate(model) for model in _AVAILABLE_AI_MODELS
]

DEFAULT_AI_MODEL: OpenAIModel = AVAILABLE_AI_MODELS[0]


def get_current_model_by_name(name: str) -> OpenAIModel:
    for model in _AVAILABLE_AI_MODELS:
        if model["name"] == name:
            return OpenAIModel.model_validate(model)

    return OpenAIModel.model_validate(DEFAULT_AI_MODEL)


# @st.cache_resource
def get_openai_client(key: Optional[str] = None):
    if (
        key is None
        and ("openai_key" in st.session_state)
        and st.session_state.openai_key
    ):
        key = st.session_state.openai_key
        return openai.OpenAI(api_key=key)

    st.warning("⚠️ Please Enter your OpenAI key to continue.")
    # st.stop()
    return None


@st.cache_data
def get_available_models() -> list[OpenAIModel]:
    client = get_openai_client()
    if client:
        res = client.models.list()
        models = []

        for model in res.data:
            if model.id.startswith("gpt-") or model.id.startswith("text-davinci"):
                is_chat_model = True if model.id.startswith("gpt-") else False
                models.append(OpenAIModel(name=model.id, is_chat_model=is_chat_model))

        return models
    return []


def is_api_key_valid(key: str) -> bool:
    client = openai.OpenAI(api_key=key)
    try:
        client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Hi"},
            ],
            max_tokens=5,
        )
    except Exception as e:
        return False
    return True


def get_selected_model():
    name: str = str(st.session_state.model_name)
    return get_current_model_by_name(name)


# Create the LLM
def get_LLM():
    key: str = str(st.session_state.openai_key)
    model: OpenAIModel = get_selected_model()
    temp: float = float(st.session_state.temp)
    max_tokens: int = int(st.session_state.max_tokens)

    return ChatOpenAI(
        model=model.name, temperature=temp, max_tokens=max_tokens, api_key=key
    )


def get_enhanced_text(text: str) -> str:
    english_level: str = st.session_state.english_level

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """In English, Please enhance the following text to be in {english_level} level.\n
                Note: Ensure to answer in Markdown format (and make important info bold).
                """,
            ),
            ("user", "Text:\n{input}"),
        ]
    )

    llm = get_LLM()
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"input": text, "english_level": english_level})


def get_my_current_text_level(text: str) -> str:
    english_level: str = st.session_state.english_level

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """In English, Please What is the english level of the following text (A1,A2,B1,B2,C1,C2)? And why?\n
                Note: Ensure to answer in Markdown format (and make important info bold).
                """,
            ),
            ("user", "Text:\n{input}"),
        ]
    )

    llm = get_LLM()
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"input": text})


def count_words(text: str) -> int:
    text = re.sub(r"[\!\?-]+", "", text)
    text = re.sub(r"\s+", " ", text)

    return len(text.split(" "))
