

## Credits to Nandha.t.me

f
from nandha import bot
from pyrogram import filters, types



import requests

SUPPORT_CHAT = -1001717881477
repo_name = 'NandhaXBOT'
repo_owner = 'NandhaxD'

commit_ids = []

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
    global commit_ids
    if len(commit_ids) == 0:
        commit_id = requests.get(api, headers=headers).json()[0]['sha']
        await send_commit_message(commit_id)
        commit_ids.append(commit_id)
    else:
        latest_commit_id = requests.get(api, headers=headers).json()[0]['sha']
        if commit_ids[0] != latest_commit_id:
            await send_commit_message(latest_commit_id)
            commit_ids.clear()
            commit_ids.append(latest_commit_id)
