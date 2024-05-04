

from nandha import bot, lang
from nandha.helpers.help_func import get as async_get
from urllib.parse import quote
from pyrogram import filters



@bot.on_message(filters.command(['bard','gpt', 'palm'], prefixes=""))
async def artificial_intelligent(_, message):
	
	if len(message.command) <2:
		return await message.reply(lang['query'])
        
	reply = await message.reply(lang['thinking'])
	model = message.text.split()[0]
	prompt = message.text.split(None, 1)[1]
	api = f"https://nandha-api.onrender.com/ai/{model}/{quote(prompt, safe='')}"	
	try:		
	    response = await async_get(api)
	    ok = response.get('content')		
	except Exception as e:
		 return await reply.edit(lang['error'].format(str(e)), parse_mode=enums.ParseMode.HTML)				
	return await reply.edit(lang['AI'].format(model.upper(), prompt, ok), parse_mode=enums.ParseMode.HTML)
