
from Katsuki import DATABASE

db = DATABASE['DEV_USERS']



async def get_users():
     list = [x['user_id'] for x in db.find()]
     return list

async def add_user(user_id: int):
    list = await get_users()
    if not user_id in list:
          user = {'user_id': user_id}
          db.insert_one(user)



async def remove_user(user_id: int):
      user = {'user_id': user_id}
      user = db.find_one(user)
      if user:
         db.delete_one(user)
      return True
      
  
  

