from fastapi import FastAPI
from app.config import settings
from app.routes.chat import router as chat_router




app = FastAPI(
    title="AgentOps Platform",
    description="Production-ready AI Agent Platform",
    version="0.1.0",
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": " AgentOps Platform is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "agentops-platform"
    }

@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }