from datetime import datetime
import telebot
from pycbrf import ExchangeRates

bot = telebot.TeleBot('Свой токен')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=7)
    itembtl1 = telebot.types.KeyboardButton('USD') #Доллар
    itembtl2 = telebot.types.KeyboardButton('EUR') #Евро
    itembtl3 = telebot.types.KeyboardButton('CNY') #Китайский юань
    itembtl4 = telebot.types.KeyboardButton('BYN') #Беларусский рубль
    itembtl5 = telebot.types.KeyboardButton('JPY') #Японская йена
    itembtl6 = telebot.types.KeyboardButton('KZT') #Казахстанский тенге
    itembtl7 = telebot.types.KeyboardButton('GBP') #Фунт стерлингов
    itembtl10 = telebot.types.KeyboardButton('О боте🤖')
    markup.add(itembtl1,itembtl2,itembtl3,itembtl4,itembtl5,itembtl6,itembtl7,itembtl10)
    bot.send_message(chat_id=message.chat.id, text='<b>Привет! Выбери нужную <i>ВАЛЮТУ</i> для просмотра <i>КУРСА</i>!</b>', reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()
    if message_norm in ['usd', 'eur', 'cny', 'byn', 'jpy', 'kzt', 'gbp',]:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id,
                        text=f'<b>{message_norm.upper()}</b> | <b>Цена:</b> <i>{float(rates[message_norm.upper()].rate)}</i> рублей',
                        parse_mode='html')
    elif message.text == 'О боте🤖':
        bot.send_message(chat_id=message.chat.id, text='Этот бот создан для отслеживания курса валют разных стран')




bot.polling(none_stop=True)

