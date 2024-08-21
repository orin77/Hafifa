from typing import Union
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Achievement(BaseModel):
    id: Optional[str]
    title: str
    description: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None
