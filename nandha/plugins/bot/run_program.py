import requests

from pyrogram import filters, types, enums, errors
from nandha import bot


langs = [
  'matl', 'matl', 'bash', 'befunge93', 'bqn', 'brachylog', 'brainfuck', 'cjam', 'clojure', 
  'cobol', 'coffeescript', 'cow', 'crystal', 'dart', 'dash', 'typescript', 'javascript', 
  'basic.net', 'fsharp.net', 'csharp.net', 'fsi', 'dragon', 'elixir', 'emacs', 'emojicode',
  'erlang', 'file', 'forte', 'forth', 'freebasic', 'awk', 'c', 'c++', 'd', 'fortran', 'go', 
  'golfscript', 'groovy', 'haskell', 'husk', 'iverilog', 'japt', 'java', 'jelly', 'julia', 
  'kotlin', 'lisp', 'llvm_ir', 'lolcode', 'lua', 'csharp', 'basic', 'nasm', 'nasm64', 'nim', 
  'javascript', 'ocaml', 'octave', 'osabie', 'paradoc', 'pascal', 'perl', 'php', 'ponylang',
  'prolog', 'pure', 'powershell', 'pyth', 'python2', 'python', 'racket', 'raku', 'retina', 
  'rockstar', 'rscript', 'ruby', 'rust', 'samarium', 'scala', 'smalltalk', 'sqlite3', 'swift', 
  'typescript', 'vlang', 'vyxal', 'yeethon', 'zig'
]

api_url = 'https://nandha-api.onrender.com/run'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


@bot.on_message(filters.command(langs, prefixes='!'))
async def interpreter(bot, message):
     m = message
     langs = m.command[0]
     ok = "!python\n```Example:\nprint('hello world')```"
     if len(m.text.split(maxsplit=1)) != 2:
          return await m.reply_text(text=ok)
     code = m.text.split(maxsplit=1)
     data = {
        'code': code,
        'lang': langs
     }
     response = requests.post(
       api_url, json=data, headers=headers
     )
     msg = await m.reply_text("⏳ Evaluating code....")
     if response.status_code == 200:
          data = response.json()
          language = data['language']
          version = data['version']
          code = data['code']
          output = data['output']
          return await msg.edit_text(
f"""\n
🌐 **Language**: `{language}`
🖥️ **Version**: `{version}`
🗨️ **Code**:\n`{code}`
✨ **Result**:\n `{output}`
""" )
     else:
        return await msg.edit_text("Something wrong with API check out 🤔")






  
         
