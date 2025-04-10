from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from handlers.buttons_handler import menu_button_handler
from handlers.message_handler import handle_message
from handlers.start_handler import start

# Запуск бота
def main():
    application = Application.builder().token("6876791960:AAHIXrKljkctg7qTosA1xxvJgPyxursPtkg").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(menu_button_handler, pattern="^donation$"))
    application.run_polling()

if __name__ == "__main__":
    main()