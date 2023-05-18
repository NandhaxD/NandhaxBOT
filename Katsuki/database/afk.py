


from Katsuki import DATABASE

db = DATABASE["AFK"]



async def add_afk(user_id: int, reason: str, datetime: datetime, is_delete: bool):	 
	 string = {"user_id": user_id, "reason": reason, "datetime": datetime, "delete": is_delete}
	 db.insert_one(string)
	 return True
	 
async def remove_afk(user_id: int):
	 string = {"user_id": user_id}
	 is_afk=db.find_one(string)
	 if is_afk:
	 	 db.delete_one(is_afk)
	 	 return True
	 return False

     	
async def update_delete(user_id: int, is_delete: bool):
     find = {"user_id": user_id}
     if db.file_one(find):
     	  update = {"$set": {"is_delete": is_delete}}
     	  db.update_one(filter=find, update=update)
               return True
     return False
     

async def is_afk(user_id: int):
	  string = {"user_id": user_id}
 	 is_afk=db.find_one(string)
   if is_afk:
 		   return True
   return False

async def get_afk_reason(user_id: int):
	  string = {"user_id": user_id}
 	 afk=db.find_one(string)
  if afk:     
     reason=afk['reason']
     return reason 
  else:
     return False
      
 
