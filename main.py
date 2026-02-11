import telebot # Обычно библиотеки для МАХ похожи на телеграмные
from telebot import types

# Вставьте сюда ТОКЕН, который вы получили в панели "МАХ для партнеров"
TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'
bot = telebot.TeleBot(TOKEN)

# Главное меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("⏰ Режим работы")
    btn2 = types.KeyboardButton("📄 Документы")
    btn3 = types.KeyboardButton("🍎 Меню")
    btn4 = types.KeyboardButton("📞 Контакты")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Здравствуйте! Я помощник детского сада. Выберите раздел:", reply_markup=markup)

# Логика ответов
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "⏰ Режим работы":
        bot.send_message(message.chat.id, "Группы работают с 07:00 до 19:00. Прием детей до 08:30.")
    elif message.text == "📄 Документы":
        bot.send_message(message.chat.id, "Для сада нужны: \n1. Заявление \n2. Мед. карта \n3. Копия паспорта.")
    elif message.text == "🍎 Меню":
        bot.send_message(message.chat.id, "Сегодня в меню: Каша молочная, Чай, Фрукты.")
    elif message.text == "📞 Контакты":
        bot.send_message(message.chat.id, "Заведующая: +7 (XXX) XXX-XX-XX\nМедсестра: +7 (XXX) XXX-XX-XX")
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял. Нажмите на кнопку в меню.")

bot.polling(none_stop=True)
