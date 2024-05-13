


from nandha import DATABASE

db = DATABASE['WELCOME']


async def set_welcome(chat_id: int, welcome: bool):
    db.update_one(
        {'chat_id': chat_id},
        {'$set': {'welcome': welcome}},
        upsert=True
    )
    return True  


async def check_welcome(chat_id: int):
    chat = {'chat_id': chat_id}
    data = db.find_one(chat)
    if data:
        welcome = data.get('welcome')
        return welcome
    else:
       return False




  
