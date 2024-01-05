from typing import Optional
from pydantic import BaseModel


class OpenAIModel(BaseModel):
	name: str
	max_tokens: Optional[int] = 4096
	is_chat_model: Optional[bool] = False
