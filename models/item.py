from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from models.pyobjectid import PyObjectId


class ItemModel(BaseModel):
    id: Optional[PyObjectId] = Field(
        default_factory=PyObjectId,
        alias="_id",
        # exclude=True
    )
    title: str
    price: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
