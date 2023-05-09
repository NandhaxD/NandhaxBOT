from Katsuki import katsuki


if __name__ == "__main__":
   katsuki.run()
   print("KATSUKI STARTED!")
   with katsuki:
          katsuki.send_message("me", text="Awake Now! 💀")

