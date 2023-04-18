import sys
import io


from subprocess import getoutput as run
import traceback

from Katsuki import katsuki
from config import ( OWNER_ID, HANDLER) 
from pyrogram import filters
from pyrogram.errors improt MessageTooLong


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)



@katsuki.on_message(filters.user(OWNER_ID) & filters.command("logs",prefixes=HANDLER))
async def logs(_, message):
       run_logs = run("tail logs.txt")
       msg = await message.reply_text("processing...")
       thumb_id = "./Katsuki/katsuki_help/IMG_20220701_185623_542.jpg"
       with io.BytesIO(str.encode(run_logs)) as logs:
            logs.name = "logs.txt"
            return await message.reply_document(
                document=logs, thumb=thumb_id
            )
       return await msg.delete()

@katsuki.on_message(filters.user(OWNER_ID) & filters.command("sh",prefixes=HANDLER))
async def sh(_, message):
    msg = await message.reply("processing...")
    code = message.text.split(message.text.split()[0])[1]
    x = run(code)
    try:
       return await message.edit_text(
             f"**SHELL**: `{code}`\n\n**OUTPUT**:\n`{x}`")
    except MessageTooLong:
         with io.BytesIO(str.encode(run_logs)) as logs:
               logs.name = "shell.txt"
               await message.reply_document(
                   document=logs, thumb=thumb_id)
               return await msg.delete()
    
@katsuki.on_message(filters.user(OWNER_ID) & filters.command("e",prefixes=HANDLER))
async def eval(client, message):
    status_message = await message.edit_text("Analyzing Code...")
    cmd = message.text.split(message.text.split()[0])[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
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
        evaluation = "Success ✅"

    final_output = "<b>EVAL</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        return await status_message.edit(final_output)


