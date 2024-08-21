from src.models.achievement import Achievement
from datetime import datetime
from config.database import get_db
from fastapi import APIRouter, HTTPException

db = get_db()


async def create_achievement(achievement: Achievement) -> Achievement:
    achievement_data = achievement.model_dump(exclude={"id"})
    achievement_data["created_at"] = datetime.now()
    result = db.achievements.insert_one(achievement_data)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to retrieve the created achievement")
    return db.achievements.find_one({"_id": result.inserted_id})


async def get_achievement(achievement_id: str) -> Achievement:
    achievement = db.achievements.find_one({"_id": achievement_id})
    if not achievement:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return achievement


async def delete_achievement(achievement_id: str) -> str:
    result = db.achievements.delete_one({"_id": achievement_id})
    if result.deleted_count:
        return "achievement deleted successfully"
    raise HTTPException(status_code=404, detail="Achievement not found")


async def update_achievement(achievement_id: str) -> int:
    result = db.achievements.delete_one({"_id": achievement_id})
    return result.deleted_count
