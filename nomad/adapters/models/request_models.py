from pydantic import BaseModel
from typing import Optional


class Place(BaseModel):
    name: str
    city: str
    pincode: str
    state: str
    rating: Optional[float] = None


class Destinations(BaseModel):
    state: str
