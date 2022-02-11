from fastapi import APIRouter, HTTPException
from starlette import status

from app.db import db
from app.models.base_model import BaseModel
from app.models.entities.comment import Comment
from app.models.object_id import PyObjectId

router = APIRouter()


class RootResponse(BaseModel):
    response: str


@router.get("/", response_model=RootResponse)
async def root():
    return RootResponse(response="Hello, world!")


class UploadBody(BaseModel):
    name: str
    comment: str


class UploadResponse(BaseModel):
    inserted_id: PyObjectId


@router.post("/upload", response_model=UploadResponse)
async def upload_comment(body: UploadBody):
    new_entry = Comment(**body.dict())
    insert_result = await db.test.insert_one(new_entry.dict())
    return UploadResponse(inserted_id=insert_result.inserted_id)


@router.get("/fetch", response_model=Comment)
async def upload_comment(comment_id: PyObjectId):
    comment_raw = await db.test.find_one({"_id": comment_id})
    if comment_raw is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    comment = Comment(**comment_raw)
    return comment
