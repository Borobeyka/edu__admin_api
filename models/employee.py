from typing import Optional
from pydantic import BaseModel, Field


class EmployeeModel(BaseModel):
    id: Optional[int] = Field(exclude=True)
    name: str
    surname: Optional[str] = None
    phone: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
