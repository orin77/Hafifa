from fastapi import APIRouter, HTTPException
from src.models.achievement import Achievement
from datetime import datetime
from config.database import get_db

router = APIRouter()

db = get_db()


@router.post('/achievements/', response_model=Achievement)
async def create_achievement(achievement: Achievement):
    achievement_data = achievement.model_dump(exclude={"id"})
    achievement_data["created_at"] = datetime.now()
    result = db.achievements.insert_one(achievement_data)
    new_achievement = db.achievements.find_one({"_id": result.inserted_id})
    if not new_achievement:
        raise HTTPException(status_code=500, detail="Failed to retrieve the created achievement")
    return new_achievement
