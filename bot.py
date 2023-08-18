import requests
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

TELEGRAM_BOT_TOKEN = "6620893650:AAGgx_QzkcgZ4pz_UZUZCpZs4NtB-PGNifQ"

bot_token = TELEGRAM_BOT_TOKEN
bot = Bot(token=bot_token)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Пожалуйста, введите ваш токен:")


def enter_bot_token(update: Update, context: CallbackContext):
    user_input = update.message.text
    chat_id = update.message.chat_id
    api_url = "http://127.0.0.1:8000/api/telegram/bindChatToUser/"
    data = {
        'token': user_input,
        'chat_id': chat_id
    }
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        update.message.reply_text("Токен успешно сохранен.")
    else:
        update.message.reply_text("Пользователь с таким токеном не существует!")

    return ConversationHandler.END


def main():
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, enter_bot_token))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
