from datetime import datetime
from typing import Optional

from bson.objectid import ObjectId
from pymongo.database import Database

from ..utils.security import hash_password


class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, user_id: str, data: dict):
        data["user_id"] = ObjectId(user_id)

        inserted_result = self.database["shanyraks"].insert_one(data)

        return inserted_result.inserted_id 

    def get_shanyrak_by_id(self, shanyrak_id: str) -> Optional[dict]:
        shanyrak = self.database["shanyraks"].find_one(
            {
                "_id": ObjectId(shanyrak_id),
            }
        )
        return shanyrak

    def update_shanyrak(self, user_id: str, data: dict):
        self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(user_id)},
            update={
                "$set": {
                    **data
                }
            },
        )

    def delete_shanyrak(self, shanyrak_id: str, user_id : str) -> Optional[dict]:
        self.database["shanyraks"].delete_one(
            {"_id": ObjectId(shanyrak_id), "user_id": ObjectId(user_id)}
        )