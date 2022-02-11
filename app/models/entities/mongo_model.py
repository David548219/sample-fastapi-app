from typing import Optional

from pydantic import Field

from app.models.base_model import BaseModel
from app.models.object_id import PyObjectId


class MongoModel(BaseModel):
    # id is marked optional, so we can construct new users without specifying one,
    # when we parse existing DB entries this is guaranteed to be present.
    id: Optional[PyObjectId] = Field(default=None, alias="_id")

    def fetch_id_from_insert(self, insert_result):
        self.id = PyObjectId(insert_result.inserted_id)

    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        if '_id' in d:
            d['id'] = d.pop('_id')
        if 'id' in d and d['id'] is None:
            del d['id']
        return d
