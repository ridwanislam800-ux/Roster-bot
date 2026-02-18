import requests
import time
import json
import random

BOT_TOKEN = "8586432055:AAHqMfo6HcTXhBj4gEz7BaSRF5pEHWqyu1g"
API = f"https://api.telegram.org/bot{BOT_TOKEN}"

roasts = [
"তুই potato brain 🤡",
"তোর মাথায় WiFi নাই",
"তুই walking lag",
"তুই error 404",
"তুই beta version মানুষ",
"তোর মাথা empty folder",
"তুই loading forever",
"তুই fake legend",
"তুই cracked human",
"তুই demo edition",
"তুই corrupted soul",
"তুই no signal brain",
"তুই lag king",
"তুই uninstall worthy",
"তুই expired logic",
"তুই buffer hero",
"তুই slow motion",
"তুই virus carrier",
"তুই update pending",
"তুই broken system",
"তুই potato elite",
"তুই brain.exe stopped",
"তুই fake premium",
"তুই human glitch",
"তুই memory leak",
"তুই blank RAM",
"তুই trial version",
"তুই discount মানুষ",
"তুই wish.com মানুষ",
"তুই loading mind",
"তুই bugged hero",
"তুই lag prince",
"তুই cracked logic",
"তুই empty soul",
"তুই potato pro",
"তুই buffering king",
"তুই offline brain",
"তুই demo mind",
"তুই fake pro",
"তুই expired update",
"তুই noob legend",
"তুই slow thinker",
"তুই broken logic",
"তুই low battery human",
"তুই error minded",
"তুই corrupted file",
"তুই uninstall life",
"তুই beta soul"
]

user_mode = {}
offset = 0

def send_msg(chat_id, text, keyboard=None):
    data = {"chat_id": chat_id, "text": text}
    if keyboard:
        data["reply_markup"] = json.dumps(keyboard)
    requests.post(f"{API}/sendMessage", data=data)

print("🤖 Bot started...")

while True:
    updates = requests.get(
        f"{API}/getUpdates",
        params={"offset": offset, "timeout": 30}
    ).json()

    for u in updates.get("result", []):
        offset = u["update_id"] + 1

        if "message" in u:
            msg = u["message"]
            chat_id = msg["chat"]["id"]
            text = msg.get("text", "")

            # /start
            if text == "/start":
                kb = {
                    "keyboard": [["Random 🔥", "Custom 😈"]],
                    "resize_keyboard": True
                }
                send_msg(chat_id, random.choice(roasts), kb)

            elif text == "Random 🔥":
                user_mode[chat_id] = "random"
                send_msg(chat_id, "Username পাঠাও 😏")

            elif text == "Custom 😈":
                user_mode[chat_id] = "custom"
                send_msg(chat_id, "নিজের roast লেখ 😈")

            else:
                if chat_id in user_mode:
                    if user_mode[chat_id] == "random":
                        send_msg(chat_id, random.choice(roasts))

                    elif user_mode[chat_id] == "custom":
                        send_msg(chat_id, "🔥 Custom Roast:\n" + text)

                else:
                    send_msg(chat_id, random.choice(roasts))

    time.sleep(1)