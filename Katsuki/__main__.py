from Katsuki import Katsuki
import config 


if __name__ == "__main__":
   Katsuki.start()
   with Katsuki:
        Katsuki.send_message(f"@{config.SUPPORT_CHAT}", "**Katsuki is Ready!**")
