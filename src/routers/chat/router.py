from fastapi import APIRouter

from routers.chat.schemas import Conversation, Messages
from tgs.graph import graph

chat_router = APIRouter()


@chat_router.post("/chat", status_code=200, tags=["Chat"])
async def conversation(
    prompt: Conversation,
) -> Messages:
    inputs = {
        "messages": [
            ("user", prompt.question),
        ]
    }
    result = graph.invoke(
        inputs,
        {"recursion_limit": 5},
    )
    return result
