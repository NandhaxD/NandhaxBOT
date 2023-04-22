
import config 
from pyrogram import filters
from Katsuki import katsuki
from requests import get

@katsuki.on_message(filters.user(config.OWNER_ID) & filters.command("check", config.HANDLER))
async def check(_, message):
    try:
       bin_code = message.command[1]
    except:
        return await message.edit("=> Enter bin code...")

    if bin_code.isnumeric():
        msg = await message.edit("=> checking bin...")
    else:
        return await message.edit("oof please input only integers")

    try:
       response = get(f"https://spamx.id/bin2/?bin={bin_code}").json()
    except Exception as e:
         return await message.edit(str(e))

    bank_name = response["bank"]["name"]
    brand = response["brand"]
    country_emoji = response["country"]["emoji"]
    country_alpha2 = response["country"]["alpha2"]
    country_currency = response["country"]["currency"]
    country_latitude = response["country"]["latitude"]
    country_longitude = response["country"]["longitude"]
    country_name = response["country"]["name"]
    country_numeric = response["country"]["numeric"]
    number = response["number"]
    prepaid = response["prepaid"]
    scheme = response["scheme"]
    type = response["type"]
    string = f"**Bank name**: {bank_name}\n"
    string += f"**Bank brand**: {brand}\n"
    string += f"**Country flag**: {country_emoji}\n"
    string += f"**Country alpha2**: {country_alpha2}\n"
    string += f"**Country currency**: {country_currency}\n"
    string += f"**Country latitude**: {country_latitude}\n"
    string += f"**Country longitude**: {country_longitude}\n"
    string += f"**Country name**: {country_name}\n"
    string += f"**Country numeric**: {country_numeric}\n"
    string += f"**Number**: {number}\n"
    string += f"**Prepaid**: {prepaid}\n"
    string += f"**Scheme**: {scheme}\n"
    string += f"**Type**: {type}\n"

    return await message.edit(string)
     

    
    
    
