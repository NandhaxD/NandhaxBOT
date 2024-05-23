import requests
from pyrogram import Client, filters, types

# Initialize your bot with the proper API credentials
from nandha import bot

import config

PLAY_HT_API_KEY = "4458780d19c84de08371651cc4ddb1eb"
PLAY_HT_USER_ID = "fMXjbY62nuZwdXsk5etM7SLlJKU2"

# Define the endpoint URL
url = "https://api.play.ht/api/v2/tts/stream"

temp = []

# Define the request headers
headers = {
    "AUTHORIZATION": PLAY_HT_API_KEY,
    "X-USER-ID": PLAY_HT_USER_ID,
    "accept": "audio/mpeg",
    "content-type": "application/json"
}

# Define the voice data
voices = {
    'benton': 's3://voice-cloning-zero-shot/b41d1a8c-2c99-4403-8262-5808bc67c3e0/bentonsaad/manifest.json',
    'navya': 's3://voice-cloning-zero-shot/e5df2eb3-5153-40fa-9f6e-6e27bbb7a38e/original/manifest.json',
    'olivia': 's3://voice-cloning-zero-shot/9fc626dc-f6df-4f47-a112-39461e8066aa/oliviaadvertisingsaad/manifest.json',
    'delilah': 's3://voice-cloning-zero-shot/1afba232-fae0-4b69-9675-7f1aac69349f/delilahsaad/manifest.json',
    'charles': 's3://voice-cloning-zero-shot/9f1ee23a-9108-4538-90be-8e62efc195b6/charlessaad/manifest.json',
    'misca': 's3://voice-cloning-zero-shot/a5cc7dd9-069c-4fe8-9ae7-0c4bae4779c5/micahsaad/manifest.json',
    'sammuel': 's3://voice-cloning-zero-shot/36e9c53d-ca4e-4815-b5ed-9732be3839b4/samuelsaad/manifest.json',
    'amelia': 's3://voice-cloning-zero-shot/34eaa933-62cb-4e32-adb8-c1723ef85097/original/manifest.json',
    'aurther': 's3://voice-cloning-zero-shot/509221d8-9e2d-486c-9b3c-97e52d86e63d/arthuradvertisingsaad/manifest.json'
}

@bot.on_message(filters.command('voice'))
async def voice(_, message):
    Usage = "Reply to a message with the text you want to convert to voice."
    user_id = message.from_user.id
    if not user_id == config.OWNER_ID and user_id in temp:
        count = temp.count(user_id)
        if count >= 7:
            return await message.reply(
                "Sorry you have generated more than 7 voices, to get more voice request ask in support chat"
            )
        else:
            temp.append(user_id)
                
    reply = message.reply_to_message
    if reply and reply.text:
        try:
            buttons = [
                types.InlineKeyboardButton(name.capitalize(), callback_data=f'voice:{user_id}:{name}') 
                for name in voices.keys()
            ]
            buttons = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]
          
            await message.reply_text(
                reply.text + "\n\n**➲ Click the voice you want ❤️**",
                reply_markup=types.InlineKeyboardMarkup(buttons)
            )
        except Exception as e:
            await message.reply_text(str(e))
    else:
        await message.reply_text(Usage)

@bot.on_callback_query(filters.regex('^voice'))
async def cb_voice(_, query):
    try:
        user_id, voice_name = query.data.split(":")[1:]
        user_id = int(user_id)
    except ValueError:
        return await query.answer('Invalid data format.')

    if query.from_user.id != user_id:
        return await query.answer('You cannot access other requests.')

    text = query.message.text.split('➲')[0].strip()
    voice_url = voices.get(voice_name)
    if not voice_url:
        return await query.message.edit(f"Invalid voice: {voice_name}")

    payload = {
        "text": text,
        "voice": voice_url,
        "output_format": "mp3",
        "speed": 1,
        "sample_rate": 44100,
        "voice_engine": "PlayHT2.0-turbo"
    }

    try:
        await query.message.edit(f"**Generating {voice_name} voice ❤️.**")

        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        chat_id = query.message.chat.id
        path = f'{user_id}{chat_id}_voice.mp3'
        with open(path, 'wb') as f:
            f.write(response.content)

        await bot.send_audio(
            chat_id=chat_id,
            audio=path,
            caption=f'**Requested by {query.from_user.mention}**',
            reply_to_message_id=query.message.id
        )
        await query.message.delete()
    except requests.RequestException as e:
        await query.message.edit(f"Request error: {e}")
    except Exception as e:
        await query.message.edit(f"Unexpected error: {e}")

