import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ваш токен из кабинета МАХ
MAX_TOKEN = 'f9LHodD0cOKJR6TZV2NRzQLNIqco7UDuPVLntAQFAuy1dKAk5pOeoKwoseF7H0Aw3R5GOAtkSi5KuZzq7OQf'
MAX_API_URL = 'https://api.max.ru/v1/send' # Уточните точный URL в доках, обычно это endpoint для сообщений

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Проверяем, что пришло сообщение
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message']['text']
        
        if text == "/start":
            send_max_message(chat_id, "Здравствуйте! Я помощник детского сада на платформе MAX.")
            
    return jsonify({"status": "ok"}), 200

def send_max_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    headers = {
        "Authorization": f"Bearer {MAX_TOKEN}",
        "Content-Type": "application/json"
    }
    requests.post(MAX_API_URL, json=payload, headers=headers)

if __name__ == '__main__':
    # Koyeb и другие сервисы используют порт 8000 или 8080
    app.run(host='0.0.0.0', port=8000)
