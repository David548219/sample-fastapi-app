from app.models.entities.mongo_model import MongoModel


class Comment(MongoModel):
    name: str
    comment: str
