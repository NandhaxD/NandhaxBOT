from Katsuki import katsuki
from pyrogram import filters
from config import ( OWNER_ID, HANDLER) 

@katsuki.on_message(filters.command("join",prefixes=HANDLER) & filters.user(OWNER_ID))
def join_chat(_, m):
          link =  m.text.split(" ")[1]
          katsuki.join_chat(link)
          m.reply_text(f"Successfully joined {link}")

@katsuki.on_message(filters.command("leave",prefixes=HANDLER) & filters.user(OWNER_ID))
def leave_chat(_, m):
          link =  m.text.split(" ")[1]
          katsuki.leave_chat(link)
          m.reply_text(f"Successfully lefted {link}")
