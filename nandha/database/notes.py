from nandha import DATABASE

db = DATABASE['NOTES']['CHATS']


async def get_chats_list() -> list:    
    chat_ids = [ chats['chat_id'] for chats in db.find() ]
    return chat_ids


           
          

  
