

from pyrogram.raw.types import UpdateMessagePollVote
from pyrogram.types import User
from pyrogram import filters, types, enums, errors
from nandha import bot as app


@app.on_raw_update(group=35)
async def poll_vote(client, update, users,  _):
    if not isinstance(update, UpdateMessagePollVote): return 
    voter = User._parse(client, users[update.user_id])
    poll_id = update.poll_id 
    choices = update.options or "retracting vote"
    await client.send_message(
      chat_id=update.chat.id,
      text=f'User {voter.first_name} voted on poll_id {poll_id} with {choices}')



@app.on_message(filters.command("sendp"))
async def SendPoll(app, message):
	      chat_id = message.chat.id
	      await app.send_poll(
	         chat_id=chat_id, 
	         question="Is this a poll question?", 
	         options=["Yes", "No", "Maybe"],
	         type=enums.PollType.QUIZ,
	         correct_option_id=1,
	         explanation="we don't know"
	         )
