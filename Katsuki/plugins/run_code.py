import sys
import io
import inspect
from contextlib import redirect_stdout


from subprocess import getoutput as run
import traceback

from Katsuki import katsuki
from config import ( OWNER_ID, HANDLER) 
from pyrogram import filters, enums
from pyrogram.errors import MessageTooLong










@katsuki.on_message(filters.command("eval",prefixes=HANDLER) & filters.user(OWNER_ID))
async def eval_command(client: katsuki, message):
        code = message.text.split(message.text.split(None,1)[0])[1]
        env = {
            "client": client,
            "message": message
        }
        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
            await message.edit_text(result)
        except Exception as ex:
            stream = io.StringIO()
            traceback.print_exc(file=stream)
            error = stream.getvalue()
            await message.edit_text(str(error))






async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)




@katsuki.on_message(filters.user(OWNER_ID) & filters.command("logs",prefixes=HANDLER))
async def logs(_, message):
       run_logs = run("tail logs.txt")
       msg = await message.edit_text("Analyzing logging...")
       thumb_id = "./Katsuki/katsuki_help/IMG_20220701_185623_542.jpg"
       with io.BytesIO(str.encode(run_logs)) as logs:
            logs.name = "logs.txt"
            await message.reply_document(
                document=logs, thumb=thumb_id
            )
       return await msg.delete()

@katsuki.on_message(filters.user(OWNER_ID) & filters.command("sh",prefixes=HANDLER))
async def sh(_, message):
    msg = await message.edit("Analyzing code...")
    try:
      code = message.text.split(message.text.split()[0])[1]
    except:
        return await message.edit("No?")
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
    await message.edit_text("Analyzing Code...")
    try:
      cmd = message.text.split(message.text.split()[0])[1]
    except:
         return await message.edit("No?")

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

    final_output = "**🖥️ Code**: "
    final_output += f"`{cmd}`\n\n"
    final_output += "**📝 Result**:\n"
    final_output += f"`{evaluation.strip()}`\n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.txt"
            await reply_to_.reply_document(
                document=out_file, caption=cmd)
            return await message.delete()
    else:
        return await message.edit_text(final_output, parse_mode=enums.ParseMode.MARKDOWN)


