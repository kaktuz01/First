from telebot import types
import telebot

bot_token = '5942330740:AAHI85jTd9HRQq7K7X_W86SEjhCmuUSi_BA'

bot = telebot.TeleBot(token=bot_token)


name = "Капибара"
energy = 70
satiety = 10
happiness = 100


def feed():
    global satiety, energy
    satiety += 10
    energy += 5


def play():
    global satiety, happiness, energy
    satiety -= 5
    happiness += 10
    energy -= 10


def sleep():
    global satiety, happiness, energy
    satiety -= 5
    happiness -= 5
    energy = 70


def check(message):
    global satiety, happiness, energy
    if satiety <= 0:
        bot.send_message(message.chat.id, f"{name} умер от голода. Не забывайте кормить питомца!")
    elif satiety >= 10:
        bot.send_message(message.chat.id, f"{name} наелся и счастлив")

    if happiness < 0:
        bot.send_message(message.chat.id, f"{name} умер от тоски. С питомцем нужно чаще играть!")
    elif happiness > 100:
        bot.send_message(message.chat.id, f"{name} счастлив как никогда")

    if energy < 50:
        bot.send_message(message.chat.id, f"{name} умрет от истощения")
    elif energy > 70:
        bot.send_message(message.chat.id, f"{name} полон сил и энергии!")


@bot.message_handler(commands=['info'])
def information(message):
    bot.send_message(message.chat.id, "Начальные характеристи твоего питомца: \nэнергия = 70 \nсытость = 10 \nсчастье "
                                      "= 100\n-----------------------\nЕсли у питомца будет меньше 50 энергии, "
                                      "то он умрет\nЕсли у питомца будет меньше 0 сытости, то он умрет\nЕсли у "
                                      "питомца будет меньше 0 счастья, то он умрет\n-----------------------\nПоесть = "
                                      "+5 к энергии\n                 + 10 к сытости\nПоиграть = -5 к сытости\n       "
                                      "          +10 к счастью\n                 -10 к энергии\nПоспать = -5 к "
                                      "сытости\n                 -5 к счастью\n                 +70 к "
                                      "энергии\nПриятной игры!")


@bot.message_handler(commands=['feed'])
def feed_handler(message):
    feed()
    bot.send_message(message.chat.id, f"{name} вкусно покушал и теперь его голод сосстовляет {satiety}!")
    check(message)


@bot.message_handler(commands=['sleep'])
def sleep_handler(message):
    sleep()
    bot.send_message(message.chat.id, f"{name} поспал и стал здоровее! Теперь его здоровье состовляет {energy}!")
    check(message)


@bot.message_handler(commands=['play'])
def play_handler(message):
    play()
    bot.send_message(message.chat.id, f"{name} поиграл и теперь его счастье состовляет {happiness}!")
    check(message)


@bot.message_handler(commands=['hp'])
def stat(message):
    global energy, satiety, happiness
    bot.send_message(message.chat.id, f'Характеристики питомцев на данный момент:\n --------------------\nЭнергия:{energy}\nСытость:{satiety}\nСчастье:{happiness}\n--------------------')


@bot.message_handler(commands=['start'])
def button(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    item_1 = types.KeyboardButton('/feed')
    item_2 = types.KeyboardButton('/play')
    item_3 = types.KeyboardButton('/sleep')
    item_4 = types.KeyboardButton('/hp')
    item_5 = types.KeyboardButton('/info')
    item_6 = types.KeyboardButton('/start')
    markup.add(item_1, item_2, item_3, item_4, item_5, item_6)
    bot.send_message(message.chat.id, 'Это игра "Создай своего питомца и ухаживай правильно за ним", что бы узнать о его начальных характеристика, и о границах нажми /info')
    bot.send_message(message.chat.id,'Выберите нужную вам команду', reply_markup=markup)


'''def emoji(message):
    if happiness == 10:
        bot.send_message(message.chat.id, '😭')
    if happiness == 20:
        bot.send_message(message.chat.id, '😱')
    if happiness == 30:
        bot.send_message(message.chat.id, '😨')
    if happiness == 40:
        bot.send_message(message.chat.id, '😩')
    if happiness == 50:
        bot.send_message(message.chat.id, '😠')
    if happiness == 60:
        bot.send_message(message.chat.id, '😌')
    if happiness == 70:
        bot.send_message(message.chat.id, '😛')
    if happiness == 80:
        bot.send_message(message.chat.id, '😚')
    if happiness == 90:
        bot.send_message(message.chat.id, '🤗')'''


bot.polling(none_stop=True)