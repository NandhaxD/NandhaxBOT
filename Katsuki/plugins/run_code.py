import sys
import io


from subprocess import getoutput as run
import traceback

from Katsuki import katsuki
from config import ( OWNER_ID, HANDLER) 
from pyrogram import filters


@katsuki.on_message(filters.user(OWNER_ID) & filters.command("logs",prefixes=HANDLER))
def logs(_, m):
       logs = run("tail logs.txt")
       msg = m.reply_text("ʟᴏɢs sᴇɴᴅɪɴɢ...")
       m.reply_document("logs.text")
       msg.delete()

@katsuki.on_message(filters.user(OWNER_ID) & filters.command("sh",prefixes=HANDLER))
def sh(_, m):
    code = m.text.replace(m.text.split(" ")[0], "")
    x = run(code)
    m.reply_text(
         f"**SHELL**: `{code}`\n\n**OUTPUT**:\n`{x}`")

    
@katsuki.on_message(filters.user(OWNER_ID) & filters.command("eval",prefixes=HANDLER))
async def eval(client, message):
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

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
        evaluation = "Success"

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
        await reply_to_.reply_text(final_output)
    await status_message.delete()


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)
