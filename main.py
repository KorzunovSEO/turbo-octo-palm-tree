import telebot
from telebot import types


bot = telebot.TeleBot('5714399659:AAEiZe48gJOunQqVGI2VSfFovSm2m-B68eQ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    lang_en = types.KeyboardButton('EN 🇺🇸')
    lang_ru = types.KeyboardButton('RU')
    lang_ua = types.KeyboardButton('UA 🇺🇦')
    markup.add(lang_ua, lang_en, lang_ru)
    bot.send_message(message.chat.id, "Choose language", reply_markup=markup)

@bot.message_handler()
def langs(message):
    if message.text == "RU":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rules1 = types.KeyboardButton('❓Почитать правила конкурса')
        rules2 = types.KeyboardButton('❗Как стать партнером')
        rules3 = types.KeyboardButton('💰Получить инвайт-ссылку')
        backbutton = types.KeyboardButton('⬅ Выбрать другой язык')
        markup.add(rules1, rules2, rules3, backbutton)
        bot.send_message(message.chat.id, "Приветствуем Вас в нашем Telegram боте! Здесь мы собрали информацию о правилах нашего конкурса и партнерской программы. Читай и зарабатывай!", reply_markup=markup)
    elif message.text == "❗Как стать партнером":
        bot.send_message(message.chat.id, 'Мы подготовили инструкцию для тебя! <a href="https://telegra.ph/Kak-zarabatyvat-vmeste-s-Crypocto-09-28">Начать зарабатывать!</a>', parse_mode='html')
    elif message.text == "⬅ Выбрать другой язык":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lang_en = types.KeyboardButton('EN 🇺🇸')
        lang_ru = types.KeyboardButton('RU 🇷🇺')
        lang_ua = types.KeyboardButton('UA 🇺🇦')
        markup.add(lang_ua, lang_ru, lang_en)
        bot.send_message(message.chat.id, "Choose language", reply_markup=markup)
    elif message.text == "💰Получить инвайт-ссылку":
        bot.send_message(message.chat.id, "Мы пришлем инвай-ссылку в личные сообщения в течении 10 минут!")
        bot.send_message(156664092, f'Пользователь с ником {message.from_user.username}, именем {message.from_user.first_name} {message.from_user.last_name} запросил инвайт ссылку.')
    elif message.text == "❓Почитать правила конкурса":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Узнать правила", url="https://t.me/c/1827261893/7"))
        bot.send_message(message.chat.id, "Подробные правила нашего конкурса", reply_markup=markup)
    elif message.text == "UA 🇺🇦":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rules1 = types.KeyboardButton('❓Дізнатись правила конкурсу')
        rules2 = types.KeyboardButton('❗Як стати партнером')
        rules3 = types.KeyboardButton('💰Отримати інвайт-посилання')
        backbutton = types.KeyboardButton('⬅ Обрати іншу мову')
        markup.add(rules1, rules2, rules3, backbutton)
        bot.send_message(message.chat.id, "Вітаємо Вас у нашому Telegram боті! Тут ми зібрали інформацію про правила нашого конкурсу та партнерської програми. Читай та заробляй!", reply_markup=markup)
    elif message.text == "❗Як стати партнером":
        bot.send_message(message.chat.id, 'Ми підготували інструкцію для тебе! <a href="https://telegra.ph/Kak-zarabatyvat-vmeste-s-Crypocto-09-28">Почати заробляти!</a>', parse_mode='html')
    elif message.text == "⬅ Обрати іншу мову":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lang_en = types.KeyboardButton('EN 🇺🇸')
        lang_ru = types.KeyboardButton('RU 🇷🇺')
        lang_ua = types.KeyboardButton('UA 🇺🇦')
        markup.add(lang_ua, lang_ru, lang_en)
        bot.send_message(message.chat.id, "Choose language", reply_markup=markup)
    elif message.text == "💰Отримати інвайт-посилання":
        bot.send_message(message.chat.id, "Ми надішлемо інвай-посилання в особисті повідомлення протягом 10 хвилин!")
        bot.send_message(156664092, f'Користувач з ніком {message.from_user.username}, ім\'ям {message.from_user.first_name} {message.from_user.last_name} запросив інвайт посилання.')
    elif message.text == "❓Дізнатись правила конкурсу":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Дізнатися правила", url="https://t.me/c/1827261893/7"))
        bot.send_message(message.chat.id, "Детальні правила нашого конкурсу", reply_markup=markup)
    elif message.text == "EN 🇺🇸":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        rules1 = types.KeyboardButton('❓Read the contest rules')
        rules2 = types.KeyboardButton('❗How to become a partner')
        rules3 = types.KeyboardButton('💰Get an invite link')
        backbutton = types.KeyboardButton('⬅ Choose another language')
        markup.add(rules1, rules2, rules3, backbutton)
        bot.send_message(message.chat.id, "Welcome to our Telegram bot! Here we have collected information about the rules of our contest and affiliate program. Read and earn!", reply_markup=markup)
    elif message.text == "❗How to become a partner":
        bot.send_message(message.chat.id, 'We have prepared a guide for you! <a href="https://telegra.ph/Kak-zarabatyvat-vmeste-s-Crypocto-09-28">Start earning!</a>', parse_mode='html')
    elif message.text == "⬅ Choose another language":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        lang_en = types.KeyboardButton('EN 🇺🇸')
        lang_ru = types.KeyboardButton('RU 🇷🇺')
        lang_ua = types.KeyboardButton('UA 🇺🇦')
        markup.add(lang_ua, lang_ru, lang_en)
        bot.send_message(message.chat.id, "Choose language", reply_markup=markup)
    elif message.text == "💰Get an invite link":
        bot.send_message(message.chat.id, "We will send an invite-link to your personal messages within 10 minutes!")
        bot.send_message(156664092, f'User with nickname {message.from_user.username}, name {message.from_user.first_name} {message.from_user.last_name} requested an invite link.')
    elif message.text == "❓Read the contest rules":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Learn the rules", url="https://t.me/c/1827261893/7"))
        bot.send_message(message.chat.id, "Detailed rules of our contest", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'The message was entered incorrectly!', parse_mode='html')



bot.polling(none_stop=True)