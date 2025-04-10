from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Функция для создания главного меню
def main_menu():
    keyboard = [
        [InlineKeyboardButton("💳 Поддержать проект", callback_data='donation')]
    ]
    return InlineKeyboardMarkup(keyboard)
