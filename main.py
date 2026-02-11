from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ваш токен МАХ (тот самый длинный)
TOKEN = 'f9LHodD0cOKJR6TZV2NRzQLNIqco7UDuPVLntAQFAuy1dKAk5pOeoKwoseF7H0Aw3R5GOAtkSi5KuZzq7OQf'

@app.route('/webhook', methods=['POST'])
def handle_max_message():
    data = request.json
    # Здесь логика: если пришло сообщение, отвечаем на него
    print("Получены данные от МАХ:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
