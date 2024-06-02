from typing import List, Optional

from openai import BaseModel
from pydantic import BaseModel


class Conversation(BaseModel):
    question: str


class Message(BaseModel):
    content: str | None
    additional_kwargs: dict | None
    response_metadata: Optional[dict] = None
    type: str | None
    name: Optional[str] = None
    id: str | None
    example: bool | None
    tool_calls: Optional[List] = []
    invalid_tool_calls: Optional[List] = []
    usage_metadata: Optional[dict] = None


class Messages(BaseModel):
    messages: List[Message]

    # @field_validator("messages", mode="before")
    # def return_last_message_content(cls, v):
    #     if v:
    #         return [v[-1]]
    #     return None
