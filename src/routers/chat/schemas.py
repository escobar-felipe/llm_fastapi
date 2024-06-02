from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Conversation(BaseModel):
    question: str


class Message(BaseModel):
    content: Optional[str] = None
    additional_kwargs: Optional[Dict[str, Any]] = None
    response_metadata: Optional[Dict[str, Any]] = None
    type: Optional[str] = None
    name: Optional[str] = None
    id: Optional[str] = None
    example: Optional[bool] = None
    tool_calls: Optional[List[Any]] = []
    invalid_tool_calls: Optional[List[Any]] = []
    usage_metadata: Optional[Dict[str, Any]] = None


class Messages(BaseModel):
    messages: List[Message]

    # @field_validator("messages", mode="before")
    # def return_last_message_content(cls, v):
    #     if v:
    #         return [v[-1]]
    #     return None
