from Katsuki import Katsuki
import config 


if __name__ == "__main__":
   Katsuki.start()
   with Katsuki:
        Katsuki.send_message(f"@{config.LOG_GROUP_ID}", "**Katsuki is Ready!**")
