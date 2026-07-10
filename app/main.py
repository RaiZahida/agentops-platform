from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.config import settings
from app.routes.chat import router as chat_router

app = FastAPI(
    title="AgentOps Platform",
    description="Production-ready AI Agent Platform",
    version="0.1.0",
)

app.include_router(chat_router)

# Enable Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "agentops-platform",
    }