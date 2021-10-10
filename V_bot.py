from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename="V_bot.log"
                    )

def greet_user(update, context):
    text = "Вызван /start"
    logging.info(text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def talk_to_me(update, context):
    if update.message.chat.last_name == None:
        user_text = "Привет, {}! Ты написал(а): {}".format(update.message.chat.first_name, 
        update.message.text)
        logging.info("User: %s, Chat id: %s, Message:%s", update.message.chat.username,
        update.message.chat.id, update.message.text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=user_text)
    else:
        user_text = "Привет, {} {}! Ты написал(а): {}".format(update.message.chat.first_name, 
        update.message.chat.last_name, update.message.text)
        logging.info("User: %s, Chat id: %s, Message:%s", update.message.chat.username,
        update.message.chat.id, update.message.text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=user_text)


def main():
    V_bot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)
    
    logging.info("Бот запускается")

    dp = V_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    V_bot.start_polling()
    V_bot.idle()

main()