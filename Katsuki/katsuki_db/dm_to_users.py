from Katsuki import DATABASE


db = DATABASE["DM"]


async get_allowed_users():
    mm = [x["user_id"] for x in db.find()]
    return mm

async def allowed_to_dm(user_id: int):
     string = {"user_id": user_id}
     if mm not in (await get_allowed_users()):
         db.insert_one(string)
         return True

async def disallowed_to_dm(user_id: int):
     bom = {"user_id": user_id}
     if db.find_one(bom):
          db.delete_one(bom)
          return True
