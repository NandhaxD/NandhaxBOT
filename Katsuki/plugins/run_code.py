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
async def terminal(client, message):
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
            await client.send_document(
                message.chat.id,
                "output.txt",
                reply_to_message_id=message.id,
                caption="`Output file`",
            )
            os.remove("output.txt")
            return
        await message.edit(f"**Output:**\n```{output}```", parse_mode="markdown")
    else:
        await message.edit("**Output:**\n`No Output`") 

    
    
@katsuki.on_message(filters.user(OWNER_ID) & filters.command("e",prefixes=HANDLER))
async def evaluate(client: katsuki , message):
    status_message = await message.edit("`Running ...`")
    try:
        cmd = message.text.split(maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    reply_to_id = message.id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message.id
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

