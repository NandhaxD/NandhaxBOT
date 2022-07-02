from config import LOG_GROUP_ID
from Katsuki import katsuki, bot
import Katsuki.plugins


if __name__ == "__main__":
   katsuki.start()
   bot.run()
   with bot:
            bot.send_message(f"{LOG_GROUP_ID}", "Katsuki Ready Boi!")

