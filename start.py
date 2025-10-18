import json
import os

def load_messages(room_code):
    filename = f"{room_code}.json"
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_message(room_code, sender, text):
    filename = f"{room_code}.json"
    messages = load_messages(room_code)
    messages.append({"from": sender, "text": text})
    with open(filename, "w") as f:
        json.dump(messages, f)

def show_messages(room_code):
    os.system("clear")
    messages = load_messages(room_code)
    print(f"\033[95mMessages from room {room_code}:\033[0m")
    for msg in messages[-10:]:
        sender = msg.get("from", "?")
        text = msg.get("text", "!")
        print(f"{sender}: {text}")

def main():
    room_code = input("\033[36mRoom code:\033[0m ")
    name = input("\033[36mYour name:\033[0m ")
    while True:
        show_messages(room_code)
        text = input("> ")
        if text.strip() == "":
            continue
        save_message(room_code, name, text)

if __name__ == "__main__":
    main()
