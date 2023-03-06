from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel


client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["AIintegration"]


class User(BaseModel):
    username: str
    email: str
    password: str
