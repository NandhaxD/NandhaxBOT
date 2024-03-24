"""
Copyright © [2023-2024] @NandhaBots. All rights reserved. Reproduction, modification, distribution, or republication of this file without prior written permission from @NandhaBots is strictly prohibited. The Katsuki Telegram user bot has been developed with the Pyrogram library and utilizing Python programming language, making it a safe and secure option for users. Unauthorized use of this bot or any part of it may result in legal action. This project is owned by @Nandha, and any unauthorized use or distribution of this bot is strictly prohibited.
"""






import sys
import io, time
import re
import os
import subprocess
import traceback
import config
from Katsuki import app, MODULE
from Katsuki.helpers.help_func import spacebin
from pyrogram import filters, enums
from pyrogram.types import Message 
from pyrogram.errors import MessageTooLong


async def aexec(code, app, m):
    exec(
        "async def __aexec(katsuki, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](app, m)


 
def p(*args, **kwargs):
    print(*args, **kwargs)
	




THUMB_ID = "./IMG_20220701_185623_542.jpg"

# get bot logging

@app.on_message(filters.me & filters.command("logs",prefixes=config.HANDLER))
async def logs(_, message):
       logsText = subprocess.getoutput("tail logs.txt")
       msg = await message.edit_text("Analyzing.....")
       if len(logsText) > 4096:
              with io.BytesIO(str.encode(logsText)) as logs:
      
                   paste = await spacebin(logsText)
                   logs.name = "logs.txt"
                   await message.reply_document(
                document=logs, captain=paste ,thumb=THUMB_ID, quote=True),
                   return await msg.delete()
       await message.edit(f"<pre>logging {logsText}</pre>", parse_mode=enums.ParseMode.HTML)


""" SHELL COMMAND ARE USED FOR PIP AND SOME MORE THOUGH """

@app.on_message(filters.me & filters.command("sh", prefixes=config.HANDLER))
async def terminal(katsuki, message):
	 
     if len(message.text.split()) <= 1:
	 	         return await message.delete()
     code = message.text.split(maxsplit=1)[1]
     output = subprocess.getoutput(code)
     final_output = f"<pre>Command:</pre><pre> {code}</pre> \n<pre language='python'>{output}</pre>"
     if len(final_output) > 4096:
     	filename = 'shell.txt'
     	file = open(filename, 'w+')
     	file.write(output)
     	file.close()
	
     	await message.reply_document(document=filename,
     	thumb=THUMB_ID, quote=True, caption=f"<code>{code}</code>", parse_mode=enums.ParseMode.HTML)
     	return await message.delete()
     else:
     	await message.edit(text=final_output, parse_mode=enums.ParseMode.HTML)




# run your codes using eval

	
@app.on_message(filters.me & filters.command("e",prefixes=config.HANDLER))
async def evaluate(app , m):
    status_message = await m.edit("`Running ...`")
    try:
        cmd = m.text.split(maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    start_time = time.time()

    	
    reply_to_id = m.id
    if m.reply_to_message:
        reply_to_id = m.reply_to_message.id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, app, m)
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
    taken_time = round((time.time() - start_time))
    
    final_output = f"<pre>Command:</pre><pre language='python'> {cmd} </pre> \n <pre> Takem time to output {taken_time}s:</pre><pre language='python'> {evaluation.strip()}</pre>"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await m.reply_document(
            document=filename,
            thumb=THUMB_ID,
            caption=cmd,
            quote=True,
            reply_to_message_id=reply_to_id,
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
