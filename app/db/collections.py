import motor.motor_asyncio as motor


class Collections:
    test: motor.AsyncIOMotorCollection

    def __init__(self, client):
        db = client.portal
        for var in vars(Collections)["__annotations__"]:
            setattr(self, var, db[var])
