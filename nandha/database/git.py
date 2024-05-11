

from nandha import DATABASE


db = DATABASE['GIT-BOT']

async def add_commit_id(id: str):
    data = {'commit_id': id}
    db.insert_one(data)
    return True

async def get_commit_ids():
    ids = [ id['commit_id'] for id in db.find() ]
    return ids
