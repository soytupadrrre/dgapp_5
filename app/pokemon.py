from datetime import datetime
from typing import List
from bson import ObjectId
from pydantic import BaseModel
from pydantic_mongo import ObjectIdField

class Pokemon(BaseModel):
    id: ObjectIdField = None
    pokedex_id: int
    name: str
    height: int
    weight: int
    atk: int
    def_: int
    atk_sp: int
    def_sp: int
    vel: int
    hp: int
    type_1: str
    type_2: str
    generation: int
    genra: str
    is_legendary: bool
    is_mythical: bool
    is_default: bool
    shape: str
    color: str
    evolution_chain: List[str]
    sprite: str
    moves: List[str]
    capture_date: datetime
    
    class Config:
        json_encoders = {ObjectId: str}
