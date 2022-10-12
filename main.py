import telebot

bot = telebot.TeleBot('5202524811:AAHk1zEhUS5vFIpYQf4Kc2BbmwoRw1QYdsI')

@bot.message_handler(commands=['op1'])
def op1(mensagem):
    bot.send_message(mensagem.chat.id, 'renan é gay')


@bot.message_handler(commands=['op2'])
def op2(mensagem):
    bot.send_message(mensagem.chat.id, 'o lucas é  gayy')


@bot.message_handler(commands=['op3'])
def op3(mensagem):
  print(mensagem)
  bot.send_message(mensagem.chat.id, 'Eai mano')


def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  text = """
  Escolha uma opção para continuar (Clique no item):
  /op1
  /op2
  /op3
  """
  bot.reply_to(mensagem, text)


bot.polling()