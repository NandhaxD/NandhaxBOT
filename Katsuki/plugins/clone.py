
from Katsuki import Katsuki
from pyrogram import filters
from katsuki_db.clone import store_my_profile

import config

@katsuki.on_message(filters.command("clone",config.HANDLER))
async def clone(_, message):
    if not message.reply_to_message:
         try:
            clone_id = message.text.split(None,1)[1]
         except:
              return await message.edit("=> reply to the user either give a user id")
    else:
         clone_id = message.reply_to_message.from_user.id

    user_id = message.from_user.id
    msg = await message.edit('collecting your current profile information.')
    heh = await katsuki.get_chat(user_id)
    bio = heh.bio
    first_name = heh.first_name
    async for photo in katsuki.get_chat_photos(user_id, limit=1):
            profile = photo.file_id
    try:
       await store_my_profile(
               user_id=user_id,
               profile=profile,
               first_name=first_name,
               bio=bio)
    except Exception as e:
           return await message.edit(f"Error in storing to db:\n{e}")
     
    
    msg = await message.edit('collecting cloner current profile information.')
    heh = await katsuki.get_chat(clone_id)
    bio = heh.bio
    first_name = heh.first_name
    async for photo in katsuki.get_chat_photos(clone_id, limit=1):
            profile = photo.file_id
    try:
       await katsuki.set_profile_photo(photo=profile)
       await katsuki.update_profile(first_name=first_name, bio=bio)
    except Exception as e:
           return await message.edit(f"Error in setting up your profile:\n{e}")
    await message.edit("Successfully Implemented")
    
    
    
    
