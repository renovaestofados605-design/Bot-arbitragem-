import requests
import time

TOKEN = "SEU_TOKEN"
CHAT_ID = "SEU_CHAT_ID"

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

while True:
    enviar("🚨 Bot funcionando!")
    time.sleep(30)
