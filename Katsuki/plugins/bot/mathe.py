



import config
import os
import requests
import io
from random import randint, choice

from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from Katsuki import bot, lang
from Katsuki.helpers.decorator import devs_only



IS_RIDDLE = False
ANSWER = {'answer': None}


          
@bot.on_message(filters.text & (~filters.private | ~filters.bot))
async def reply_riddle_answer(_, message):
     global ANSWER
     if IS_RIDDLE:
          try:
             answer = int(ANSWER['answer'])
             if int(message.text) == answer:
                  await message.reply('You guess the answer 🥳, wait for next riddle.')
                  ANSWER['answer'] = None
      

async def get_question():     
     symbol = ['+','-','*']
     query = "({num1}{syb1}{num2}){syb2}{num3}".format(num1=randint(20, 44), syb1=choice(symbol), num2=randint(2, 9), syb2=choice(symbol), num3=randint (1, 30))     
     result = eval(query)
     return {'query': query, 'result': result}

async def make_math_riddle(text: str):
     img = Image.open(io.BytesIO(requests.get("https://graph.org/file/9b165baf9de57406d76ca.jpg").content))
     draw = ImageDraw.Draw(img)
     url = "https://github.com/JulietaUla/Montserrat/raw/master/fonts/otf/Montserrat-ExtraBold.otf"
     k = requests.get(url)
     open(url.split("/")[-1], "wb").write(k.content)
     font = ImageFont.truetype(url.split("/")[-1], size=100)
     math = await get_question()
     question = math['query'] + " = ?"
     answer = math['result']
     tbox = font.getbbox(question)
     w = tbox[2] - tbox[0]
     h = tbox[3] - tbox[1]
     # Set the center of the image as the position for the text
     width, height = img.size
     position = (width // 2, height // 2)
     color = (255, 255, 255)
     draw.text(((width-w)//2, (height-h)//2), question, font=font, fill=color)
     img = img.resize((int(width*1.5), int(height*1.5)), Image.LANCZOS)
     name = "maths_quiz.jpg"
     img.save(name)    
     return name, question, answer 


async def send_math_riddle(text: str, chat_id: int):
         global ANSWER 
         while count < 21:
              if IS_RIDDLE == False:
                   return await message.reply(
                        'Riddle Stopped 🔴')
              elif count == 20:
                   return await message.reply(
                         'All riddle finished for new start do `/riddle on`')
              nandha = await make_math_riddle(text)
              ANSWER['answer'] = nandha[2]
              await bot.send_photo(
                    photo=nandha[0],  caption=nandha[1])
              os.remove(nandha[0])
              asyncio.sleep(2*60)


@bot.on_message(filters.command('riddle'))
@devs_only
async def riddle(_, message):
     global IS_RIDDLE
     if len(message.text.split()) < 2:
           return await message.reply(
                'Example: `/riddle on|off`')
     condition = message.text.split()[1].lower()
     if condition == 'on':
            IS_RIDDLE = True
            await message.reply('Starting riddle...')
     elif condition == 'off':
            if IS_RIDDLE == False:
                      return await message.reply('No active riddle.')
            else:
                await message.reply('Stopping riddle..')
                IS_RIDDLE = False
          
     else:
          return await message.reply(
               'Example: `/riddle on|off`')
          
     

     



"""
template = requests.get("https://graph.org/file/9b165baf9de57406d76ca.jpg")
     with open("image.jpg", "wb") as img_file:
           img_file.write(template.content)
     img = Image.open("image.jpg")
     draw = ImageDraw.Draw(img)
     url = "https://github.com/JulietaUla/Montserrat/raw/master/fonts/otf/Montserrat-ExtraBold.otf"
     font = ImageFont.truetype(urllib.request.urlopen(url), size=100)
     position = (270, 300)
     color = (255, 255, 255)
     draw.text(position, text, font=font, fill=color)
     img.save('boom.jpg')
     
"""

                    
    # Wait for the print thread to finish before exiting the programo
