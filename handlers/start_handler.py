from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from keyboards.main_menu import main_menu

# Начальная команда, отображающая кнопки
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Данный бот позволяет скачивать видео из соцсетей по ссылке. Бот полностью бесплатный, но вы можете поддержать автора рублём! Для использования просто отправь ссылку на видео!",
        reply_markup=main_menu()
    )

start_handler = CommandHandler("start", start)
