from fastapi import APIRouter, HTTPException
from src.models.achievement import Achievement
from config.database import get_db
from src.controllers.achievements_controller import create_achievement

router = APIRouter()

db = get_db()


@router.post('/achievements/', response_model=Achievement)
async def create_achievement(achievement: Achievement):
    new_achievement = create_achievement(achievement)
    if not new_achievement:
        raise HTTPException(status_code=500, detail="Failed to retrieve the created achievement")
    return new_achievement
