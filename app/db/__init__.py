import motor.motor_asyncio as motor

from app.config import MONGO_URI
from app.db.collections import Collections

client = motor.AsyncIOMotorClient(MONGO_URI)
db = Collections(client)
