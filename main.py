import telebot
from telebot import types
from config import TOKEN
from config import image

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	keyboardinlain = types.InlineKeyboardMarkup()
	keyboardinlain.add(
		types.InlineKeyboardButton(text='Перейти в ВИП',callback_data='startMess')
		)
	bot.send_photo(message.chat.id, open(image,'rb'),reply_markup=keyboardinlain)
	


if __name__ == '__main__':
	bot.polling()