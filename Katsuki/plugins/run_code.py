import sys
import io

from subprocess import getoutput as run
import traceback

from Katsuki import katsuki
from config import ( OWNER_ID, HANDLER) 
from pyrogram import filters, enums
from pyrogram.errors import MessageTooLong



async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)




@katsuki.on_message(filters.user(OWNER_ID) & filters.command("logs",prefixes=HANDLER))
async def logs(_, message):
       run_logs = run("tail logs.txt")
       msg = await message.edit_text("Analyzing Logging...")
       thumb_id = "./Katsuki/katsuki_help/IMG_20220701_185623_542.jpg"
       with io.BytesIO(str.encode(run_logs)) as logs:
            logs.name = "logs.txt"
            await message.reply_document(
                document=logs, thumb=thumb_id
            )
       return await msg.delete()


@katsuki.on_message(filters.user(OWNER_ID) & filters.command("sh",prefixes=HANDLER))
async def sh(_, message):

    await message.edit("Analyzing Code...")
    
    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    if len(message.text.split()) == 0:
           return await message.edit("can you input the code to run program?")

    code = message.text.split(message.text.split()[0])[1]        
    x = run(code)

    try:

       await reply_to_.reply_text(f"**🖥️ Code**: ```{code}```\n\n**📝 Results**:\n```{x}```")
       return await message.delete()

    except MessageTooLong:
         with io.BytesIO(str.encode(run_logs)) as logs:
               logs.name = "shell.txt"

               await reply_to_.reply_document(
                   document=logs, thumb=thumb_id)

               return await message.delete()

    
@katsuki.on_message(filters.user(OWNER_ID) & filters.command("e",prefixes=HANDLER))
async def evaluate(client: katsuki , message):
    status_message = await message.edit("`Running ...`")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    reply_to_id = message.id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message.id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
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
        evaluation = "Success"
    final_output = f"<b>Command:</b>\n<code>{cmd}</code>\n\n<b>Output</b>:\n<code>{evaluation.strip()}</code>"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document=filename,
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await status_message.delete()
        return
    else:
        await status_message.edit(final_output)
        return 

