

#credit to @NandhaxD

from Katsuki import DATABASE

db = DATABASE["CLONE"]



async def store_profile(user_id: int, profile: str, first_name: str, bio: str):
      filter = {"user_id": user_id}
      if not db.find_one(filter):
           string = {"user_id": user_id,"profile": profile,"first_name": first_name, "bio": bio}
           db.insert_one(string)
           return 
      else:
           update = {"$set": {"profile": profile,"first_name": first_name, "bio": bio}}
           db.update_one(filter , update)
           return 


async def get_profile(user_id: int):
     katsuki = {"user_id": user_id}
     if katsuki:
          dict = db.find_one(katsuki)
          return dict
     return False
          
    
