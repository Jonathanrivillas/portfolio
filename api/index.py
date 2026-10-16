from fastapi import FastAPI
import json
from api.schemas import SkillGroup

app = FastAPI(
    title="Portfolio API", description="API for my portfolio website", version="1.0.0"
)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/skills", response_model=list[SkillGroup])
def get_skills():
    with open("api/data/skills.json", encoding="utf-8") as f:
        return json.load(f)
