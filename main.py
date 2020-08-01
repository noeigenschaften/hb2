import telebot
from dialog import Dialog

token = '1351830053:AAEkiLssf5ceqMUDBWvTdiulX9wUc0HdVPA'

bot = telebot.TeleBot(token=token)

print(f'Your token is: {token}')
print('Start pooling...')

dialog_instance = Dialog(bot, {
    'voc': 'voc.yaml',
})

dialog_instance.start()
