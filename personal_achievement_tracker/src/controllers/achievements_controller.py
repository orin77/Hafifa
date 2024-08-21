from src.models.achievement import Achievement
from datetime import datetime
from config.database import get_db

db = get_db()


async def create_achievement(achievement: Achievement):
    achievement_data = achievement.model_dump(exclude={"id"})
    achievement_data["created_at"] = datetime.now()
    result = db.achievements.insert_one(achievement_data)
    return db.achievements.find_one({"_id": result.inserted_id})
