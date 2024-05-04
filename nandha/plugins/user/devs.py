"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""






import sys
import io
import time
import re
import os
import subprocess
import traceback
import requests as req
import config
import pyrogram
from nandha import app, MODULE, bot, lang
from nandha.helpers.help_func import spacebin as paste
from nandha.helpers.decorator import devs_only
from pyrogram import filters, enums
from pyrogram.types import Message 
from pyrogram.errors import MessageTooLong


async def aexec(code, app, message, m, r, my, chat, ruser, bot):
    exec(
        "async def __aexec(app, message, m, r, ruser, my, chat, bot): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](app, message, m, r, ruser, chat, my, bot)


 
def p(*args, **kwargs):
    print(*args, **kwargs)
	




THUMB_ID = "./IMG_20220701_185623_542.jpg"

# get bot logging

@app.on_message(~filters.bot & filters.me & filters.command("logs",prefixes=config.PREFIXES))
async def Getlogs(_, message):
       logsText = subprocess.getoutput("tail logs.txt")
       msg = await message.edit_text(lang['alyz'])
       if len(logsText) > 4094:
              with io.BytesIO(str.encode(logsText)) as logs:
                   logs.name = "logs.txt"
                   await message.reply_document(
                document=logs,thumb=THUMB_ID, quote=True),
                   return await msg.delete()
       return await message.edit(lang['logging'].format(logsText), parse_mode=enums.ParseMode.HTML)


#HELL COMMAND ARE USED FOR PIP AND SOME MORE THOUGH 

@app.on_message(~filters.bot & filters.me & filters.command("sh", prefixes=config.PREFIXES))
async def run_shell(katsuki, message):
	 
     if len(message.text.split()) <= 1:
	 	         return await message.delete()
     code = message.text.split(maxsplit=1)[1]
     output = subprocess.getoutput(code)
     final_output = lang['shell_01'].format(code, output)
     if len(final_output) > 4095:
     	filename = 'shell.txt'
     	file = open(filename, 'w+')
     	file.write(output)
     	file.close()
	
     	await message.reply_document(document=filename,
     	thumb=THUMB_ID, quote=True, caption=lang['shell_02'].format(code), parse_mode=enums.ParseMode.HTML)
     	return await message.delete()
     else:
     	await message.edit(text=final_output, parse_mode=enums.ParseMode.HTML)




# run your codes using eval

	
@app.on_message(~filters.bot & filters.me & filters.command("e",prefixes=config.PREFIXES))
async def evaluate(app , message):
    
    status_message = await message.edit("`Running ...`")
    try:
        cmd = message.text.split(maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    start_time = time.time()

    r = message.reply_to_message	
    m = message
    ruser = getattr(r, 'from_user', None)
    my = getattr(message, 'from_user', None)
    chat = getattr(message, 'chat', None)

    if r:
        reply_to_id = r.id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(
		code=cmd, 
		app=app, 
		m=message, 
		r=r,
		chat=chat,
		message=message,
		ruser=ruser,
		my=my,
		bot=bot
	)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    taken_time = round((time.time() - start_time), 3)
    output = evaluation.strip()
	
    final_output = lang['eval_01'].format(cmd, taken_time, output)
	
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document=filename,
            thumb=THUMB_ID,
            caption=cmd,
            quote=True,
            
        )
        os.remove(filename)
        await status_message.delete()
        return
    else:
        await status_message.edit(final_output, parse_mode=enums.ParseMode.HTML)
        return 



__mod_name__ = "Dev" 
  
__help__ = """
- e: evaluate codes
- sh: shell codes
- logs: logging info
""" 
  
 
string = {"module": __mod_name__, "help": __help__}
MODULE.append(string)
