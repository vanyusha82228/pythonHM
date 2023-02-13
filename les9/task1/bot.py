from telegram import Bot, Update 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


bot = Bot(token="")

updater =  Updater(token = "" )
dispatcher = updater.dispatcher

def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, "Привет \n как дела?\nПришли мне сообщения и я удалю изи него слова с 'абв'")

def cut_command(update: Update, context: CallbackContext):
    user_msg = update.message.text.split()
    # new_text = {} 
    # for el in user_msg:
    #     if  not "абв"  in el:
    #         new_text.append(el)
    text_to_send = [el for el in user_msg if not 'абв' in el]
    context.bot.send_message(update.effective_chat.id, ' '.join(text_to_send))

start_handler = CommandHandler('start', start_command)
message_handler = MessageHandler(Filters.text, cut_command)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

print('server start')
updater.start_polling()
updater.idle()