import telebot

bot = telebot.TeleBot('5202524811:AAHk1zEhUS5vFIpYQf4Kc2BbmwoRw1QYdsI')

@bot.message_handler(commands=['op1'])
def op1(mensagem):
    bot.send_message(mensagem.chat.id, 'renan é gay')

@bot.message_handler(commands=['beneficios'])
def beneficios(mensagem):
  bot.send_audio(mensagem.chat.id, open('benefi.mp3', 'rb'))  

@bot.message_handler(commands=['promo'])
def promo(mensagem):
  bot.send_audio(mensagem.chat.id, open('isumsm.mp3', 'rb'))

def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  text = """
  Escolha uma opção para continuar (Clique no item):
  /promo
  /beneficios
  """
  bot.reply_to(mensagem, text)


bot.polling()