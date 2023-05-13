import sys
import io
import re
import os
import subprocess
import traceback
import config
from Katsuki import app
from pyrogram import filters, enums
from pyrogram.errors import MessageTooLong


async def aexec(code, app, message):
    exec(
        "async def __aexec(katsuki, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](app, message)



THUMB_ID = "./IMG_20220701_185623_542.jpg"

@app.on_message(filters.me & filters.command("logs",prefixes=HANDLER))
async def logs(_, message):
       run_logs = subprocess.getoutput("tail logs.txt")
       msg = await message.edit_text("Analyzing Logging...", quote=True)       
       with io.BytesIO(str.encode(run_logs)) as logs:
            logs.name = "logs.txt"
            await message.reply_document(
                document=logs, thumb=THUMB_ID, quote=True
            )
       return await msg.delete()


@app.on_message(filters.me & filters.command("sh", prefixes=HANDLER))
async def terminal(katsuki, message):
	 
     if len(message.text.split()) <= 1:
	 	         return await message.delete()
     code = message.text.split(maxsplit=1)[1]
     output = subprocess.getoutput(code)
     if len(output) > 4096:
     	filename = 'shell.txt'
     	file = open(filename, 'w+')
     	file.write(output)
     	file.close()
     	await message.reply_document(document=filename,
     	thumb=THUMB_ID, quote=True, caption=f"`{code}`", parse_mode=enums.ParseMode.MARKDOWN)
     	return await message.delete()
     else:
     	string = f"""\n
Command:
`{code}`

Results:
`{output}`
"""
     	await message.edit(text=string, parse_mode=enums.ParseMode.MARKDOWN)



    
@app.on_message(filters.me & filters.command("e",prefixes=HANDLER))
async def evaluate(app , message):
    status_message = await message.edit("`Running ...`", quote=True)
    try:
        cmd = message.text.split(maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    reply_to_id = message.id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, katsuki, message)
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
    final_output = f"<b>Command:</b>\n<code>{cmd}</code>\n\n<b>Output</b>:\n<code>{evaluation.strip()}</code>"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document=filename,
            thumb=THUMB_ID,
            caption=cmd,
            disable_notification=True, quote=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await status_message.delete()
        return
    else:
        await status_message.edit(final_output)
        return 

