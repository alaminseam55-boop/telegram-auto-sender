import time
import requests

BOT_TOKEN = "8608793202:AAFoIeTiaDbGlx2PqLtduwo0EwAjKJaPrOA"  # আপনার বটের টোকেন

# যে যে গ্রুপে মেসেজ যাবে তাদের Chat ID
CHAT_IDS = [
    "-1003562542602",
    "-1002595375335",
    "-1002673164624",
    # বাকি সব Chat ID কমা দিয়ে নিচে নিচে বসাবেন
]

# যে মেসেজটি বারবার পাঠানো হবে
MESSAGE = "সবাই কেমন আছেন?"

# কতক্ষণ পরপর মেসেজ যাবে (সেকেন্ডে হিসাব)
# ৬০ সেকেন্ড = ১ মিনিট, ৩০০ সেকেন্ড = ৫ মিনিট, ৩৬০০ সেকেন্ড = ১ ঘণ্টা
INTERVAL = 2

def send_messages():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for chat_id in CHAT_IDS:
        payload = {
            "chat_id": chat_id,
            "text": MESSAGE,
            "parse_mode": "HTML"
        }
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f"Error for {chat_id}: {e}")
        time.sleep(1)  # স্প্যাম ব্লক এড়াতে গ্রুপগুলোর মাঝে ১ সেকেন্ড বিরতি

if __name__ == "__main__":
    print("অটোমেটিক ব্রডকাস্ট চালু হয়েছে...")
    while True:
        send_messages()
        time.sleep(INTERVAL)
