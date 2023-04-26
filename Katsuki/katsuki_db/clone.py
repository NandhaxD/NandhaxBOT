

#credit to @NandhaxD

from Katsuki import DATABASE

db = DATABASE["clone"]


async def get_user_ids():
     user_ids = [x["user_id"] for x in db.find()]
     return user_ids

async def store_my_profile(user_id: int, profile: str, first_name: str, bio: str):
      if not user_id in (await get_user_ids()):
            string = {"user_id": user_id,"profile": profile,"first_name": first_name, "bio": bio}
            db.insert_one(string)
            return True
      return False

async def get_my_profile(user_id: int):
     if not user_id in (await get_user_ids()):
           return False
     else:
         query = {"user_id": user_id}
         object = db.find_one(query)
         return object

    
