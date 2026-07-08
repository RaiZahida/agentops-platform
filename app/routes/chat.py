from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm import LLMService

router = APIRouter()

llm_service = LLMService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = llm_service.generate_response(request.message)

    return ChatResponse(
        response=response
    )