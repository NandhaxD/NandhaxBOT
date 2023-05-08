import sys
import io
import re
import os
import subprocess
import traceback
from Katsuki import katsuki
from config import ( OWNER_ID, HANDLER) 
from pyrogram import filters, enums
from pyrogram.errors import MessageTooLong



async def aexec(code, katsuki, message):
    exec(
        "async def __aexec(katsuki, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](katsuki, message)



THUMB_ID = "./IMG_20220701_185623_542.jpg"

@katsuki.on_message(filters.user(OWNER_ID) & filters.command("logs",prefixes=HANDLER))
async def logs(_, message):
       run_logs = run("tail logs.txt")
       msg = await message.edit_text("Analyzing Logging...")       
       with io.BytesIO(str.encode(run_logs)) as logs:
            logs.name = "logs.txt"
            await message.reply_document(
                document=logs, thumb=THUMB_ID
            )
       return await msg.delete()


@katsuki.on_message(filters.user(OWNER_ID) & filters.command("sh",prefixes=HANDLER))
async def terminal(katsuki, message):
    if len(message.text.split()) == 1:
        await message.edit(f"Usage: `.sh echo owo`")
        return
    args = message.text.split(None, 1)
    teks = args[1]
    if "\n" in teks:
        code = teks.split("\n")
        output = ""
        for x in code:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            except Exception as err:
                print(err)
                await message.edit(
                    """
**Error:**
```{}```
""".format(
                        err
                    )
                )
            output += "**{}**\n".format(code)
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", teks)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type, value=exc_obj, tb=exc_tb
            )
            await message.edit("""**Error:**\n```{}```""".format("".join(errors)))
            return
        output = process.stdout.read()[:-1].decode("utf-8")
    if str(output) == "\n":
        output = None
    if output:
        if len(output) > 4096:
            with open("output.txt", "w+") as file:
                file.write(output)
            await katsuki.send_document(
                message.chat.id,
                document="output.txt",
                thumb=THUMB_ID,
                reply_to_message_id=message.id,
                caption="`Output file`",
            )
            os.remove("output.txt")
            return
        return await message.edit(f"**Output:**\n```{output}```", parse_mode=enums.ParseMode.MARKDOWN)
    else:
        return await message.edit("**Output:**\n`No Output`") 

    
    
@katsuki.on_message(filters.user(OWNER_ID) & filters.command("e",prefixes=HANDLER))
async def evaluate(katsuki , message):
    status_message = await message.edit("`Running ...`")
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
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await status_message.delete()
        return
    else:
        await status_message.edit(final_output)
        return 

