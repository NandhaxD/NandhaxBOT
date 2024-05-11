

## Credits to Nandha.t.me


from nandha import bot, DATABASE
from pyrogram import filters, types


import requests



is_commit = False #okda

db = DATABASE['GIT-BOT']

async def add_commit_id(id: str):
    data = {'commit_id': id}
    db.insert_one(data)
    return True

async def get_commit_id():
    data = db.find_one({})
    if data and data['commit_id']:
         return [data['commit_id']]
        

async def del_commit_id():
    data = db.find_one({})
    if data and data['commit_id']:
         return db.delete_one(data)
    
        
    


SUPPORT_CHAT = -1001717881477
repo_name = 'NandhaXBOT'
repo_owner = 'NandhaxD'


api = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
repo_url = f'https://gitHub.com/{repo_owner}/{repo_name}'
commit_url = repo_url + '/commit/'

headers = {
    'Authorization': 'token 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',
    'Accept': 'application/vnd.github.v3+json'
}

String = (
  '**[💫 New Commit]({}):**\n'
  '**Author**: {}\n'
  '**Committer**: {}\n'
  '**Email**: {}\n'
  '**Date**: {}\n\n'
  '**Message**:\n{}'
)

async def send_commit_message(commit_id):
    rsp = requests.get(api, headers=headers).json()
    commit_data = rsp[0]['commit']
    author = commit_data['author']['name']
    committer = commit_data['committer']['name']
    email = commit_data['committer']['email']
    date = commit_data['committer']['date']
    msg = commit_data['message']
    url = commit_url + commit_id
    button = [[types.InlineKeyboardButton(text='Vist Commit 👀', url=url)]]
    await bot.send_message(
        chat_id=SUPPORT_CHAT,
        text=String.format(repo_url, author, committer, email, date, msg),
        reply_markup=types.InlineKeyboardMarkup(button)
    )


@bot.on_message(filters.chat(SUPPORT_CHAT) & ~filters.bot, group=3)
async def notify_commit(_, message):
    global is_commit
    if not is_commit:
        commit_id = requests.get(api, headers=headers).json()[0]['sha']
        await send_commit_message(commit_id)
        await add_commit_id(commit_id)
        is_commit = True
    else:
        latest_commit_id = requests.get(api, headers=headers).json()[0]['sha']
        if (await get_commit_id()) != latest_commit_id:
            await send_commit_message(latest_commit_id)
            await del_commit_id()
            await add_commit_id(latest_commit_id)
            is_commit = True
