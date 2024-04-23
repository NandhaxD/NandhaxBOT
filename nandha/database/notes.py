from nandha import DATABASE

db = DATABASE['NOTES']['CHATS']


async def get_chats_list() -> list:    
    chat_ids = [ chats['chat_id'] for chats in db.find() ]
    return chat_ids


async def add_note(chat_id, data):
      save_data = {
          'chat_id': chat_id,
          'notes': [data]
     }
      db.insert_one(save_data)
      return True

       
      


           
          

  
