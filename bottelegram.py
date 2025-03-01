from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("7691195372:AAHYpSTJvf1mWsK7tVW3FbUHZV5SCneYC9s")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"Bot nhận được tin nhắn: {text}")
    return "OK", 200

@app.route('/')
def index():
    return "Bot đang chạy trên Render!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

