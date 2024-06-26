

from pyrogram.raw.types import UpdateMessagePollVote
from pyrogram.types import User
from pyrogram import filters, types, enums, errors
from nandha import bot as app


@app.on_raw_update(group=9996)
async def r_poll_answer_s(client, update, users, chats):
    print(update)
    print(users)
    print(chats)
    if isinstance(update, UpdateMessagePollVote):
        print("{:0>2x}".format(update.options[0][0]))
    raise ContinuePropagation
  
@app.on_raw_update(group=35)
async def poll_vote(client, update, users, chats):
 #   if not isinstance(update, UpdateMessagePollVote)
    voter = User._parse(client, users[update.user_id])
    poll_id = update.poll_id 
    choices = update.options or "retracting vote"
    print(str(update))
    await client.send_message(
      chat_id=chats.id,
      text=f'User {voter.first_name} voted on poll_id {poll_id} with {choices}'
    )



@app.on_message(filters.command("sendp"))
async def SendPoll(app, message):
	      chat_id = message.chat.id
	      await app.send_poll(
	         chat_id=chat_id, 
	         question="Is this a poll question?", 
	         options=[
             types.PollOption(text="Yes"),
             types.PollOption(text="No"),
             types.PollOption(text="Maybe")
           ],
	         type=enums.PollType.QUIZ,
	         correct_option_id=1,
	         explanation="we don't know"
	         )
