import asyncio 

from Katsuki import katsuki 
from config import OWNER_ID, HANDLER
from pyrogram import filters
from gpytranslate import Translator

import requests


@katsuki.on_message(filters.command(["ud","define"],prefixes=HANDLER) & filters.user(OWNER_ID))
async def ud(_, message):
        if len(message.command) < 2:
             return await message.edit("where you input the text?")         
        text = message.text.split(None, 1)[1]
        try:
          results = requests.get(
            f'https://api.urbandictionary.com/v0/define?term={text}').json()
          reply_text = f'**results: {text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        except Exception as e: 
              return await message.edit_text(f"Somthing wrong Happens:\n`{e}`")
        ud = await message.edit_text("Exploring....")
        await ud.edit_text(reply_text)
        
        
trans = Translator()
@katsuki.on_message(filters.command("tr",prefixes=HANDLER) & filters.user(OWNER_ID))
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("[Reply To The Message Using The Translation Code Provided!](https://telegra.ph/Lang-Codes-03-19-3)")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"**Translated from {source} to {dest}**:\n"
        f"`{translation.text}`"
    )
    await message.delete()
    await reply_msg.reply_text(reply)
    return 

@katsuki.on_message(filters.command("cc",HANDLER) & filters.user(OWNER_ID))
async def fake_cc(_, m):
     try:
        code = m.command[1]
     except:
         return await m.edit("=> Input the bin code")
     api = requests.get(f"https://spamx.id/gen/?bin={code}&limit=50").json()
     cc = ""
     credits = api["Gen"]
     for x in credits:
         cc += f"{x}\n"
     bank = api.get("Bin Info")
     bank_name = bank.get("bank")
     bin_code = bank.get("bin")
     country = bank.get("country")
     flag = bank.get("flag")
     ios = bank.get("ios")
     level = bank.get("level")
     prepaid = bank.get("prepaid")
     type = bank.get("type")
     vendor = bank.get("vendor")
     string = f"""\u0020
=> BIN DETAILS:
🏦 **Bank**: {bank_name}
💳 **Bin**: {bin_code}
🌍 **Country**: {country}
⁉️ **Flag**: {flag}
📛 **Ios**: {ios}
⬆️ **Level**: {level}
🧐 **Prepaid**: {prepaid}
🧮 **Type**: {type}
❤️ **Vendor**: {vendor}\n

=> **HERE CREDIT CARDS**:
{cc}
"""
     return await m.edit(string)
    


    
@katsuki.on_message(filters.command("fk",HANDLER) & filters.user(OWNER_ID))
async def fake(_, m):
    res = requests.get("http://spamx.id/fake/").json()
    name = "{}, {} {}".format(res["name"]["title"], res["name"]["first"], res["name"]["last"])
    cell = res.get("cell")
    country = res.get("location").get("country")
    postcode = res.get("location").get("postcode")
    state = res.get("location").get("state")
    latitude = res.get("location").get("coordinates").get("latitude")
    longitude = res.get("location").get("coordinates").get("longitude")
    gender = res.get("gender")
    email = res.get("email")
    age = res.get("dob").get("age")
    date = res.get("dob").get("date")
    street_number = res.get("location").get("street").get("number")
    street_name = res.get("location").get("street").get("name")
    phone = res.get("phone")
    uuid = res.get("login").get("uuid")
    sha256 = res.get("login").get("sha256")
    md5 = res.get("login").get("md5")
    sha1 = res.get("login").get("sha1")
    salt = res.get("login").get("salt")
    password = res.get("login").get("password")
    string = f"""\u0020
📎 **FAKE ACCOUNT DETAILS**:
=> **Name**: {name}
=> **Age**: {age}
=> **BirthDay**: {date}
=> **Gender**: {gender} 
=> **Email**: {email}
=> **Logins**:
Passward: {password}
Uuid: {uuid}
Sha256: {sha256}
Sha1: {sha1}
Salt: {salt}
Md5: {md5}
=> **Cell**: {cell}
=> **Phone**: {phone}
=> **Street**:
Name: {street_name}
Number: {street_number}
=> **State**: {state}
=> **Country**: {country}
=> **Postcode**: {postcode}
=> **Latitude**: {latitude}
=> **Longitude**: {longitude}
"""
    return await m.edit(string)



    



      
     

