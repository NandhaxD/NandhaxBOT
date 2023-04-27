
from Katsuki import katsuki
from pyrogram import filters
from Katsuki.katsuki_db.clone import store_my_profile, get_user_ids, get_my_profile

import config

@katsuki.on_message(filters.command("clone",config.HANDLER) & filters.user(config.OWNER_ID))
async def clone(_, message):
    if not message.reply_to_message:
         try:
            clone_id = message.text.split(None,1)[1]
         except:
              return await message.edit("=> reply to the user either give a user id")
    else:
         clone_id = message.reply_to_message.from_user.id

    user_id = message.from_user.id
    
    if user_id not in (await get_user_ids())
          msg = await message.edit('collecting your profile information.')
          heh = await katsuki.get_chat(user_id)
          bio = heh.bio
          first_name = heh.first_name
          profile = heh.photo.big_file_id

          try:
             await store_my_profile(user_id=user_id,profile=profile,first_name=first_name,bio=bio)
          except Exception as e:
                  return await message.edit(f"🚫 Error in storing to db:\n{e}")
           
    await msg.edit('collecting cloner profile information.')
    heh = await katsuki.get_chat(clone_id)
    bio = heh.bio
    first_name = heh.first_name
    profile = await katsuki.download_media(heh.photo.big_file_id)

    try:
       await katsuki.set_profile_photo(photo=profile)
       await katsuki.update_profile(first_name=first_name, bio=bio)
    except Exception as e:
           return await msg.edit(f"🚫 Error in setting up your profile:\n{e}")

    return await msg.edit("✅ Successfully Implemented")
    
    
    
@katsuki.on_message(filters.command("rnclone", config.HANDLER) & filters.user(OWNER_ID))
async def return_clone(_, message):
      user_id = message.from_user.id
      if user_id not in (await get_user_ids()):
           return message.edit("You never clone's someone first clone yet!")
      else:
          details = await get_my_profile(user_id)
          try:
             bio = details['bio']
             first_name = details['first_name']
             photo = details['profile"]
          except Exception as e:
                 return await message.edit(f"Yeh somthing wrong in getting your information:\n{e}")
         profile = await katsuki.download_media(photo)
         try:
            await katsuki.set_profile_photo(photo=profile)
            await katsuki.update_profile(first_name=first_name, bio=bio)
         except Exception as e:
              return await message.edit(f"🚫 Error in setting up your profile:\n{e}")

         return await message.edit("✅ Successfully Implemented")
    
       


