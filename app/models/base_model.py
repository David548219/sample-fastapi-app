from pydantic import BaseModel as PydanticBaseModel

from app.utils.custom_json_encoders import custom_encoders


class BaseModel(PydanticBaseModel):
    class Config:
        allow_population_by_field_name = True
        json_encoders = custom_encoders
