
import config
from pyrogram import filters, enums
from pyrogram.types import ChatPrivileges
from Katsuki import katsuki


@katsuki.on_message(filters.command(["promote","fpromote"], prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def promote_member(_, message):
     #promote a member to be admin in chat
     if message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
     else:
        try:
           user_id = message.command[1]
        except:
            return await message.edit("Input username either id!")
     my_privileges = await message.chat.get_member(user_id=message.from_user.id) 
     if my_privileges.privileges:
           can_promote_members = my_privileges.privileges.can_promote_members
           if not can_promote_members:
                    return await message.edit("You don't add admin right imfao.")               
     else:
         return await message.edit('You are not admin anyway.')
     command = message.command[0]
     if command == "fpromote":
            try:
                await message.chat.promote_member(user_id=user_id, privileges=my_privileges)
                return await message.edit("=> Fully Promoted! (:")
            except:
                pass
     elif command == "promote":
             privileges = ChatPrivileges(
                        can_delete_messages=True, can_restrict_members=True,
                        can_change_info=True, can_invite_users=True, can_pin_messages=True)
             try:
                await message.chat.promote_member(user_id=user_id, privileges=privileges)
                return await message.edit("=> Promoted! (:")
             except:
                 pass      


@katsuki.on_message(filters.command(["pin","unpin"], prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def messages_pin(_, message):
      """ Reply to Messages for pin either unpin """
      if not message.reply_to_message:
           return await message.edit("No Reply?")
      else:
         try:
            command = message.text[1:].casefold()
         except Exception as e:
              return await message.edit_text(f"Somthing Wrong Happens:\n{e}")
         link = message.reply_to_message.link
         if command == "pin":    
             try:
                 await message.reply_to_message.pin()
             except Exception as e:
                 return await message.edit_text(f"Somthing Wrong Happens:\n{e}")
             return await message.edit("Done!")
         elif command == "unpin":
               try:
                   await message.reply_to_message.unpin()
               except Exception as e:
                   return await message.edit_text(f"Somthing Wrong Happens:\n{e}")
               return await message.edit("Done!")


@katsuki.on_message(filters.command("invite", prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def invite_link(_, message):
     chat_id = message.chat.id
     try:
        link = (await katsuki.get_chat(chat_id)).invite_link
     except Exception as e: 
         return await message.edit(f"Somthing Wrong Happens:\n{e}")
     return await message.edit(str(link))

@katsuki.on_message(filters.command("admins", prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def admins_list(_, message):
     """Get Chat Administrators"""
     chat_id = message.chat.id
     title = message.chat.title
     msg = await message.edit("Analyzing Admins...")
     mm = f"👮 Admins ( in {title} ):\n"
     try:
        async for m in katsuki.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
              if m.user.is_bot != True:
                    mm += f" => [{m.user.first_name}](tg://user?id={m.user.id})\n"
     except Exception as e:
           return await msg.edit(f"Somthing Wrong Happens:\n{e}")
     return await msg.edit(mm)
     

@katsuki.on_message(filters.command("del", prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def delete_message(_, message):
     """delete reply to the message and itself"""
     if message.reply_to_message:
         try:
            await message.reply_to_message.delete()
         except Exception as e:
              return await message.edit(f"Somthing wrong Happens:\n{e}")
         return await message.delete()
     else:
         return await message.edit("No Reply?")



@katsuki.on_message(filters.command("ban", prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def ban_member(_, message):
    """Ban the user from chat"""
    if message.reply_to_message:
         user_id = message.reply_to_message.from_user.id  
    else:
      try:
         user_id = message.text.split()[1]
      except:
          return await message.edit("Provide USER_ID To Ban!")
    try:
       owo = await message.chat.ban_member(user_id)
    except Exception as e:
        return await message.edit(f"Somthing wrong Happens:\n{e}")
    name = (await katsuki.get_users(user_id)).first_name
    return await message.edit(f"=> {name} Has Been Banned!")


@katsuki.on_message(filters.command("unban", prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def unban_member(_, message):
    """UnBan the user from Chat"""
    if message.reply_to_message:
         user_id = message.reply_to_message.from_user.id  
    else:
      try:
         user_id = message.text.split()[1]
      except:
          return await message.edit("Provide USER_ID To UnBan!")
    try:
       owo = await message.chat.unban_member(user_id)
    except Exception as e:
        return await message.edit(f"Somthing wrong Happens:\n{e}")
    name = (await katsuki.get_users(user_id)).first_name
    return await message.edit(f"=> {name} Has Been UnBanned!")


@katsuki.on_message(filters.command("purge", prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def purge(_, message):
    """Purge Message(s) Reply to"""
    chat_id = message.chat.id
    if not message.reply_to_message:
        return await message.edit_text("No Reply?")
    else:
        reply_msg_id = message.reply_to_message.id
        message_id = message.id
        message_ids = []
        for ids in range(reply_msg_id, message_id):
            message_ids.append(ids)
        try:
           await katsuki.delete_messages(chat_id=chat_id, message_ids=message_ids)
        except Exception as e:
              return await message.edit(f"Somthing wrong Happens:\n{e}")
        return await message.edit(f"=> Purged {len(message_ids)} Message(s)")
       

