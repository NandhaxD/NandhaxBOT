import config
from Katsuki import Katsuki as bot
import Katsuki.plugins


if __name__ == "__main__":
   katsuki.start()
   bot.run()
   with bot:
            bot.send_message(f"{config.LOG_GROUP_ID}", "Katsuki Ready Boi!")

