import methods as m
from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram_api import dispatcher, updater
import logging

# Логирование, пока все в общий файл
logging.basicConfig(level=logging.INFO, filename='logger.txt', filemode='a', encoding='utf-8',
                    format='%(asctime)s %(levelname)s %(message)s')

#У бота есть меню, сделано через BotFather

starting = 0
doing = 1
doing_or_cancel = 2


# Вводное сообщение
def help_bot(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! Это бот калькулятор, смотри возможности в меню!')
    return starting


#Старт программы
def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Начинаем калькулятор! Введите выражение для счета: ')
    return doing


#Выполнение программы
def do_it(update, context):
    text = update.message.text
    chat_id = update.message.chat_id
    primer = m.parse(text)
    result = m.calculate(primer)
    context.bot.send_message(update.effective_chat.id, f'Результат равен : {result}!')
    logging.info(f'Пользователь: {chat_id}; {text} = {result}')
    return ConversationHandler.END


#Отмена программы
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'До встречи!')


help_handler = CommandHandler('help', help_bot)
start_handler = CommandHandler('start', start)
button_handler = MessageHandler(Filters.text, do_it)
cancel_handler = CommandHandler('cansel', cancel)


conv_handler = ConversationHandler(entry_points=[help_handler],
                                    states={starting: [start_handler],
                                            doing: [button_handler]},
                                    fallbacks=[cancel_handler])


dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()
