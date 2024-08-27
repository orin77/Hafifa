from fastapi import APIRouter, HTTPException

from src.models import achievement
from src.models.achievement import Achievement
from config.database import get_db
from src.controllers.achievements_controller import create_achievement, get_achievement, delete_achievement, \
    update_achievement

router = APIRouter()

db = get_db()


@router.post('/achievements/', response_model=Achievement)
async def create_achievement(achievement: Achievement) -> Achievement:
    return await create_achievement(achievement)


@router.get('/achievements/{achievement_id}', response_model=Achievement)
async def get_achievement(achievement_id: str) -> Achievement:
    return await get_achievement(achievement_id)


@router.delete('/achievements/{achievement_id}', response_model=str)
async def delete_achievement(achievement_id: str) -> str:
    return await delete_achievement(achievement_id)


@router.put('/achievements/{achievement_id}', response_model=Achievement)
async def update_achievement(achievement_id: str) -> achievement:
    return await update_achievement(achievement_id)

