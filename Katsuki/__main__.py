from Katsuki import katsuki, app

async def run_clients():
      await app.start()
      await katsuki.start()
      await pyrogram.idle()


if __name__ == "__main__":
    katsuki.loop.run_until_complete(run_clients())
