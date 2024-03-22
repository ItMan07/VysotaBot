from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_kb():
    # keyboard = InlineKeyboardMarkup()
    # keyboard.add(
    #     # InlineKeyboardButton('Создать отчет', callback_data='create_report'),
    #     InlineKeyboardButton('Создать отчет', callback_data='create_report')
    # )
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton('Создать отчет')
    )
    return keyboard


def cancel_kb():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton('Отмена')
    )
    return keyboard
