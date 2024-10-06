


#funny nodule


import random

from pyrogram import filters
from nandha import bot


CMDS = [ 'howall', 'stress', 'cringe', 'cute', 'anger', 'wish', 'happy', 'sex', 'beauty', 'boobs', 'dick', 'horny', 'gay', 'lezbian', 'noob', 'idiot', 'nigga', 'pro'] 

sex_string = [
  'Wanna sex with me? {}.',
  'Sorry you\'r pussy aren\'t that taste {}.'
]

@bot.on_message(filters.command(CMDS))
async def howall(_, message):
    reply = message.reply_to_message
    if reply:
        mention = reply.from_user.mention
    else:
        mention = message.from_user.mention

    reply_func = reply if reply else message
    query = message.command[0]
    if query == 'howall':
          text = "**Commands**:\n"
          for i, string in enumerate(CMDS):
             if string == 'howall':
                 continue
             text += f"{i}, {string}\n"
          return await reply_func.reply_text(text)
      
    elif query == 'sex':
          return await reply_func.reply_text(random.choice(sex_string).format(mention))
    else:
        num = random.randint(0, 100)
        default = f'**You\'re {num}% {query} {mention}**'
        url_data = {
            'gay': 'https://telegra.ph//file/489199eab5a922b1e6529.mp4',
            'lezbian': 'https://telegra.ph//file/1d185a148783f364f1ee8.mp4',
            'horny': 'https://telegra.ph//file/1597814837d4f60d6944e.mp4',
            'dick': 'https://telegra.ph//file/3e270d488a6e09ea6e902.mp4',
            'boobs': 'https://telegra.ph//file/6cdb0450dcbc457a9e48f.mp4',
            'noob': 'https://telegra.ph//file/8e4d7e3213ab240f9df0b.mp4',
            'idiot': 'https://telegra.ph//file/71b56eee6b5f4b46d89bb.mp4',
            'nigga': 'https://telegra.ph//file/0e9acff8b61039a857d90.mp4',
            'beauty': 'https://graph.org/file/5f2e2de605dabcba88250.mp4',
            'pro': 'https://graph.org/file/4148eee2228b6932b87d8.mp4',
            'happy': 'https://graph.org/file/97a4255b12507d6afd107.mp4',
            'wish': 'https://graph.org/file/71a3426dd84e096378c4c.mp4',
            'stress': 'https://graph.org/file/108ba0615e1aae6ee512f.mp4',
            'anger': 'https://graph.org/file/9d8d7d0782082acdd1016.mp4',
            'cute': 'https://graph.org/file/d18acc7b969a2a519fc47.mp4',
            'cringe': 'https://graph.org/file/78822c1d45414ccb5e0d7.mp4'
        }
        if query in url_data:
            url = url_data[query]
            return await reply_func.reply_animation(
                animation=url, caption=default
            )


__module__ = "Howall"

__help__ = """

✨ **How all bot inspiration commands**:

'stress', 'cringe', 'cute', 'anger', 'wish', 
'happy', 'sex', 'beauty', 'boobs', 'dick',
'horny', 'gay', 'lezbian', 'noob',
'idiot', 'nigga', 'pro'

Reply to the user or do check self.

"""
