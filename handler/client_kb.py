from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3

).add(
    KeyboardButton("отмена")
)
submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3

).add(
    KeyboardButton("да"),
    KeyboardButton("заново"),
    KeyboardButton("отмена")
)