from telegram.ext import CallbackContext
from telegram import Update


async def menu_button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "donation":
        await query.message.reply_text(
        "👏 Спасибо за поддержку!\n"
        "💀 Вы можете перевести любую сумму по реквизитам ниже:\n\n"
        "`2202205099773324` - сбер\n\n",
    parse_mode="Markdown"
)
