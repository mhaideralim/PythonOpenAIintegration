import openai
from fastapi import APIRouter
from model import User, db
from ai_integration import generate_text

router = APIRouter()
openai.api_key = "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"


@router.get("/")
async def hello_world(email: str):
    await db.users.find_one({"user": email})
    response = {
        "code": 1,
        "message": "Hello World",
        "data": email
    }
    return response


@router.post("/users")
async def create_user(user: User):
    # save user to MongoDB
    await db.users.insert_one(user.dict())

    # generate welcome message using OpenAI
    welcome_message = await generate_text(f"Hello, {user.username}!")

    return {"message": welcome_message}
