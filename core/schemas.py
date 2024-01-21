from typing import Optional

from pydantic import BaseModel


class OpenAIModel(BaseModel):
    name: str
    max_tokens: int = 4096
    is_chat_model: Optional[bool] = False

    def __str__(self) -> str:
        return self.name
