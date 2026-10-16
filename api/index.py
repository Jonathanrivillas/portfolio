from fastapi import FastAPI

app = FastAPI(title="Portfolio API", description="API for my portfolio website", version="1.0.0")


@app.get("/api/health")
def health_check():
    return {"status": "ok"}