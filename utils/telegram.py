import requests
import json
import os
# import socket

# print(socket.gethostbyname("api.telegram.org"))

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.json'))

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def send_telegram_message(message):
    config = load_config()
    token = config['tel_token']
    chat_id = config['tel_chatid']
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data=payload, timeout=5)
        # print(f"status code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(e)
# send_telegram_message("hi")















# import requests
# import json
# import os
# import socket

# CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.json'))

# def load_config():
#     with open(CONFIG_PATH, 'r') as f:
#         return json.load(f)

# def send_telegram_message(message):
#     config = load_config()
#     token = config['tel_token']
#     chat_id = config['tel_chatid']
#     url = f"https://api.telegram.org/bot{token}/sendMessage"  # ✅ درست شد
#     payload = {"chat_id": chat_id, "text": message}
#     try:
#         print("🔍 api.telegram.org →", socket.gethostbyname("api.telegram.org"))
#         response = requests.post(url, data=payload, timeout=1)
#         print(f"✅ status code: {response.status_code}")
#         print(f"📦 response: {response.text}")
#     except requests.exceptions.RequestException as e:
#         print("⛔ خطا در ارسال:", e)

# if __name__ == "__main__":
#     send_telegram_message("✅ الان درست کار می‌کنه!")
