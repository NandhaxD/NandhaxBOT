
import asyncio


async def send_auto_del_msg(client, method, chat_id: int, text, reply_to_message_id: int, time: int = 7):
    # await send_auto_del_msg(bot, 'message', chat.id, 'ok', None, 5)
  
    method_name = f'send_{method}'
    if hasattr(client, method_name):
        send_method = getattr(client, method_name)
        if method == 'message':
            msg = await send_method(chat_id=chat_id, text=text, reply_to_message_id=reply_to_message_id)
            await asyncio.sleep(time)
            await msg.delete()
        else:
            msg = await send_method(chat_id=chat_id, caption=text, reply_to_message_id=reply_to_message_id) 
            await asyncio.sleep(time)
            await msg.delete()
    else:
        return False

    
