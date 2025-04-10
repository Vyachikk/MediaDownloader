import os
from telegram import Update
from telegram.ext import MessageHandler, filters, CallbackContext
from services.download_service import download_video, is_supported_url

async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.strip()

    if is_supported_url(text):
        await update.message.reply_text("⬇️ Идет скачивание...")
        video_path = download_video(text)
        if video_path:
            with open(video_path, 'rb') as video_file:
                await update.message.reply_video(video_file)
            os.remove(video_path)
        else:
            await update.message.reply_text("❌ Не удалось скачать видео. Возможно, ссылка недействительна.")
    else:
        await update.message.reply_text("📎 Отправьте ссылку на видео. Поддерживаются: YouTube, VK, Instagram Reels, TikTok и др.")

message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
