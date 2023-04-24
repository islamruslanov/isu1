from aiogram import Dispatcher, types
from canfig import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# @dp.callback_query_handler(text="quiz_1_button")
async def quiz_2(cull: types.CallbackQuery):
    markup_2 = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton('next', callback_data="quiz_2_button")
    markup_2.add(button_2)
    question = 'Столица Канады'
    answer = [
        'Оттава',
        "Канберра",
        "Вена",
        "Мехико,"
    ]
    await bot.send_poll(
        chat_id=cull.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        reply_markup=markup_2
    )


# @dp.callback_query_handler(text='quiz_2_button')
async def quiz_3(cull: types.CallbackQuery):
    question = 'Столица японии '
    answer = [
        "Пеккин ",
        "Сеул ",
        "Токио",
        "Мехико"
    ]
    await bot.send_poll(
        chat_id=cull.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="quiz_1_button")
    dp.register_callback_query_handler(quiz_3, text="quiz_2_button")
