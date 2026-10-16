from pydantic import BaseModel


class LocalizedText(BaseModel):
    es: str
    en: str


class SkillGroup(BaseModel):
    category: LocalizedText
    items: list[str]
