from pydantic import BaseModel
from typing import Optional


class Place(BaseModel):
    name: str
    city: str
    pincode: str
    state: str
    opening_time: str
    closing_time: str
    dest_genre: str
    rating: Optional[float] = None
    text: Optional[str] = None


class Destinations(BaseModel):
    state: str
