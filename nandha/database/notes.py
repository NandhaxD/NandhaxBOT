from nandha import DATABASE

db = DATABASE['NOTES']['CHATS']


async def get_chats_list() -> list:    
    chat_ids = [ chats['chat_id'] for chats in db.find() ]
    return chat_ids


async def get_notes_list(chat_id: int):
    chat = db.find_one({'chat_id': chat_id})
    if chat:
        notes = [ note['name'] for note in chat['notes'] ]
        return notes

async def add_note(chat_id, data):
      notes = db.find_one({'chat_id': chat_id})
      if len(notes['notes']) > 0:
           db.update_one(
               {'chat_id': chat_id}, 
               {'$push': {'notes': data}}
            )
           return True
      else:
          save_data = {
          'chat_id': chat_id,
          'notes': [data] 
          }
          db.insert_one(save_data)
          return True

       
      


           
          

  
