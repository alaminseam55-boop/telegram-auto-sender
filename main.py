import os
import random
import threading
import time
from datetime import datetime
from flask import Flask
import requests

# ১. Render ও UptimeRobot-এর জন্য ব্যাকগ্রাউন্ড ওয়েব সার্ভার
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


# ২. টেলিগ্রাম কনফিগারেশন
BOT_TOKEN = "8608793202:AAFoIeTiaDbGlx2PqLtduwo0EwAjKJaPrOA"  # আপনার বটের টোকেন বসান

CHAT_IDS = [
    "-1003562542602",
    "-1002595375335",
    "-1002673164624",
    # আপনার চ্যানেলের Chat ID এখানে দিন
]

# ধাপ ১ থেকে কপি করা ছবির লিংকটি এখানে বসান
IMAGE_URL = "https://i.postimg.cc/g06KHrvR/1787907380226.jpg"

INTERVAL = 2  # প্রতি ২ সেকেন্ড পরপর মেসেজ পাঠাবে

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


def generate_caption():
    random_name = random.choice(NAMES)
    random_user_id = "".join([str(random.randint(0, 9)) for _ in range(10)])
    random_price = random.randint(100, 1000)
    current_date = datetime.now().strftime("%d/%m/%Y")

    caption = f"""🔔 <b>𝐍𝐄𝐖  𝐏𝐔𝐑𝐂𝐇𝐀𝐒𝐄𝐃</b> 🕸

👤 <b>ইউজার:</b> {random_name} 
🆔 <b>ইউজার আইডি:</b> {random_user_id} 
📦 <b>প্রোডাক্ট:</b> Sms Eye Rat
💰 <b>প্রাইজ:</b> ৳ {random_price} 
📅 <b>তারিখ:</b> {current_date}

━━━━━━━━━━━━━━━━━━
🚀  <b>𝐁ᴏ𝐭 𝐒𝐭𝐨𝐫𝐞 XS</b> ✅"""
    return caption


def send_photo_post():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    caption_text = generate_caption()

    for chat_id in CHAT_IDS:
        payload = {
            "chat_id": chat_id,
            "photo": IMAGE_URL,
            "caption": caption_text,
            "parse_mode": "HTML",
        }
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f"Error for {chat_id}: {e}")


def bot_loop():
    while True:
        send_photo_post()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    keep_alive()  # ওয়েব সার্ভার রান করবে
    bot_loop()  # ছবি ও মেসেজ পাঠানো শুরু করবে
