import requests
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

TELEGRAM_BOT_TOKEN = "6620893650:AAGgx_QzkcgZ4pz_UZUZCpZs4NtB-PGNifQ"

bot_token = TELEGRAM_BOT_TOKEN
bot = Bot(token=bot_token)

ENTER_BOT_TOKEN = range(1)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Пожалуйста, введите ваш tgBotToken:")
    return ENTER_BOT_TOKEN


def enter_bot_token(update: Update, context: CallbackContext):
    user_input = update.message.text
    context.user_data['token'] = user_input
    chat_id = update.message.chat_id
    api_url = "http://127.0.0.1:8000/api/telegram/setTgBotTokenToUser/"
    data = {
        'token': user_input,
        'chat_id': chat_id
    }
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        update.message.reply_text("tgBotToken успешно сохранен.")
    else:
        update.message.reply_text("Ошибка при сохранении tgBotToken.")

    return ConversationHandler.END


def main():
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ENTER_BOT_TOKEN: [MessageHandler(Filters.text & ~Filters.command, enter_bot_token)]
        },
        fallbacks=[],
    )

    dp.add_handler(conversation_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
