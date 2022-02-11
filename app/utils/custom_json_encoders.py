from uuid import UUID

from bson import ObjectId

from app.models.object_id import PyObjectId


def encode_object_id(id):
    return str(id)


def encode_uuid(uuid):
    return str(uuid)


custom_encoders = {
    ObjectId: encode_object_id,
    PyObjectId: encode_object_id,
    UUID: encode_uuid
}
