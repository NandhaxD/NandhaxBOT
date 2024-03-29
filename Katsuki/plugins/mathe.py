
import config
import os
import requests
import urllib
from random import randint, choice

from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from Katsuki import app, lang



async def get_question():
     api = "https://newton.vercel.app/api/v2/simplify/{query}"
     symbol = ['+','-','*']
     query = "({num1}{syb1}{num2}){syb2}{num3}".format(num1=randint(20, 44), syb1=choice(symbol), num2=randint(2, 9), syb2=choice(symbol), num3=randint (1, 30))
     response = requests.get(api.format(query)).json()
     result = response['result']
     return { 'query': query, 'result': result }
     

@app.on_message(filters.me & filters.command('riddle', prefixes=config.HANDLER))
async def math_riddle(_, message):
     msg = await message.edit(lang['thinking'])
     template = requests.get("https://graph.org/file/9b165baf9de57406d76ca.jpg")
     with open("image.jpg", "wb") as img_file:
           img_file.write(template.content)
     img = Image.open("image.jpg")
     draw = ImageDraw.Draw(img)
     url = "https://github.com/JulietaUla/Montserrat/raw/master/fonts/otf/Montserrat-ExtraBold.otf"
     font = ImageFont.truetype(urllib.request.urlopen(url), size=100)
     math = await get_question()
     text = math['query'] + " = ?"
     answer = math['result']
     position = (270, 300)
     color = (255, 255, 255)
     draw.text(position, text, font=font, fill=color)
     img.save('boom.jpg')
     try:
           await m.reply_photo(
               photo='boom.jpg', 
                       caption=lang['riddle'].format(query, result))
           await msg.delete()
     except Exception as e:
           await msg.edit(lang['error'].format(e))
     os.remove("image.jpg")
     os.remove("boom.jpg")
     
