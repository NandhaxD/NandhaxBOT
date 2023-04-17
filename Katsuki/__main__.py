from Katsuki import katsuki


if __name__ == "__main__":
   katsuki.start()
   with katsuki:
          katsuki.send_message("me", text="Awake Now! 💀")

