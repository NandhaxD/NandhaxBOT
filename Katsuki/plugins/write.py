import os
import config

from pyrogram import filters 
from PIL import Image, ImageFont, ImageDraw
from Katsuki import katsuki


@katsuki.on_message(filters.command("write",prefixes=config.HANDLER) & filters.user(config.OWNER_ID))
async def writing(_, message):
     REPLY=message.reply_to_message
     if not REPLY:
        if len(message.text.split()) == 1:
             return await message.edit('`.write hello`')
        text = message.text.split(maxsplit=1)[1]
     else:
         if not REPLY.caption and not REPLY.text:
              return await message.edit('reply to message only!')
         text = REPLY.caption or REPLY.text
     
        
     img_width = 800
     img_height = 600
     font_size = 30
     # Replace with your preferred font file path
     font_path = "./Please write me a song.ttf"         
         
     # Set parameters: image size, font, text, line spacing, margins

     line_spacing = 1.2
     top_margin = 50
     left_margin = 50

     # Create image, font, and draw objects
     img = Image.new("RGB", (img_width, img_height), (255, 255, 255))
     font = ImageFont.truetype(font_path, font_size)
     draw = ImageDraw.Draw(img)

     # Split text into lines and calculate y positions
     lines = text.split("\n")
     y_pos = top_margin
     for line in lines:
     # Draw text line by line with line spacing
          draw.text((left_margin, y_pos), line, font=font, fill=(0, 0, 0))
          y_pos += int(font.getsize(line)[1] * line_spacing)

     # Show or save image
     img.show()
     path = "write.jpg"
     img.save(path)
     if os.path.exists(path):
           await message.reply_photo(photo=path)
           os.remove(path)
           return await message.delete()
     else:
        return await message.edit("PATH DOESN'T EXISTS.")
          
