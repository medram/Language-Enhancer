import openai
import streamlit as st

from streamlit_extras.switch_page_button import switch_page
from core.schemas import OpenAIModel


LANGUAGE_LEVELS = [
	"A1",
	"A2",
	"B1",
	"B2",
	"C1",
	"C2"
]

_AVAILABLE_AI_MODELS = [
	{ "name": "gpt-3.5-turbo",           "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-3.5-turbo-0301",      "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-3.5-turbo-0613",      "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-3.5-turbo-1106",      "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-3.5-turbo-16k",       "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-3.5-turbo-16k-0613",  "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-4",                   "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-4-0314",              "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-4-0613",              "max_tokens": 4096, "is_chat_model": True },
    { "name": "gpt-4-1106-preview",      "max_tokens": 4096, "is_chat_model": True },
    { "name": "text-davinci-003",        "max_tokens": 4096, "is_chat_model": False },
    { "name": "text-curie-001",          "max_tokens": 4096, "is_chat_model": False },
]

#@st.cache_resource
def get_openai_client(key: str = None):

	if key is None and ("openai_key" in st.session_state) and st.session_state.openai_key:
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


AVAILABLE_AI_MODELS = [model.name for model in get_available_models()]


def is_api_key_valid(key: str) -> bool:
	client = openai.OpenAI(api_key=key)
	try:
		client.chat.completions.create(
		  model="gpt-3.5-turbo",
		  messages=[
			{"role": "system", "content": "Hi"},
		  ],
		  max_tokens=5
		)
	except Exception as e:
		return False
	return True

