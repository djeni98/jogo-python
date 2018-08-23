from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import my

updater = Updater(token=my.token)

dispatcher = updater.dispatcher


## bot.send_message(chat_id="[...]", text="[xyz]") é a mesma coisa que
## update.message.reply_text("[xyz]")

## functions

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Olá, bora jogar Foda-se?")

def help_fun(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ajuda em andamento...")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def args_teste(bot, update, args):
	try:
		for i, j in enumerate(args):
			update.message.reply_text("Você digitou: " + args[i])
	except:
		update.message.reply_text("Você não digitou nada após o comando /args")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Comando desconhecido")

## handlers
start_handler = CommandHandler('start', start) #(/start, function start)
help_handler = CommandHandler('help', help_fun)
echo_handler = MessageHandler(Filters.text, echo) # echo non-command text messages

args_handler = CommandHandler('args', args_teste, pass_args=True)

unknown_handler = MessageHandler(Filters.command, unknown)


## dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(args_handler)

dispatcher.add_handler(unknown_handler)

## start bot
updater.start_polling()

updater.idle()
