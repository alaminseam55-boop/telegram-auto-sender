import os
import random
import threading
import time
from datetime import datetime
from flask import Flask
import requests

# ১. UptimeRobot ও Render এর জন্য ওয়েব সার্ভার
app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is active 24/7!"


def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()


# ২. টেলিগ্রাম বট কনফিগারেশন
BOT_TOKEN = "8608793202:AAFoIeTiaDbGlx2PqLtduwo0EwAjKJaPrOA"  # আপনার বট টোকেন দিন

CHAT_IDS = [
    "-1003562542602",
    "-1002595375335",
    "-1002673164624",
]

INTERVAL = 2  # প্রতি ২ সেকেন্ড পরপর মেসেজ যাবে

# র্যান্ডম নামের তালিকা
NAMES = [
    "Rahim Ahmed",
    "Karim Ullah",
    "Tanvir Hasan",
    "Sabbir Hossain",
    "Al Amin",
    "Shakib Khan",
    "Mehedi Hasan",
    "Arif Rahman",
    "Nafis Iqbal",
    "Rony Talukder",
    "Imran Nazir",
    "Sohanur Rahman",
    "Hasan Mahmud",
    "Ashikur Rahman",
]


def generate_message():
    # র্যান্ডম ডেটা তৈরি
    random_name = random.choice(NAMES)
    random_user_id = "".join([str(random.randint(0, 9)) for _ in range(10)])
    random_price = random.randint(100, 1000)

    # বর্তমান তারিখ (দিন/মাস/বছর)
    current_date = datetime.now().strftime("%d/%m/%Y")

    # আপনার ফরম্যাট অনুযায়ী মেসেজ
    text = f"""🔔 <b>𝐍𝐄𝐖  𝐏𝐔𝐑𝐂𝐇𝐀𝐒𝐄𝐃</b> 🕸

👤 <b>ইউজার:</b> {random_name} 
🆔 <b>ইউজার আইডি:</b> {random_user_id} 
📦 <b>প্রোডাক্ট:</b> Sms Eye Rat
💰 <b>প্রাইজ:</b> ৳ {random_price} 
📅 <b>তারিখ:</b> {current_date}

━━━━━━━━━━━━━━━━━━
🚀  <b>𝐁ᴏ𝐭 𝐒𝐭𝐨𝐫𝐞 XS</b> ✅"""
    return text


def send_messages():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    message_text = generate_message()

    for chat_id in CHAT_IDS:
        payload = {"chat_id": chat_id, "text": message_text, "parse_mode": "HTML"}
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f"Error for {chat_id}: {e}")


def bot_loop():
    while True:
        send_messages()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    keep_alive()  # ব্যাকগ্রাউন্ড ওয়েব সার্ভার চালু
    bot_loop()  # মেসেজ পাঠানো চালু
