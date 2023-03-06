from dotenv import load_dotenv

load_dotenv()

import os

API_KEY = os.getenv("openai.api_key")
MongoURL = os.getenv("MONGO_CONNECTION_STRING")
