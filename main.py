import telebot

bot = telebot.TeleBot('5202524811:AAHk1zEhUS5vFIpYQf4Kc2BbmwoRw1QYdsI')



def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  bot.reply_to(mensagem, 'Olá aqui é o Bot do Rafudo')

bot.polling()