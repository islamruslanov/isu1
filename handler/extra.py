from aiogram import Dispatcher, types
from canfig import bot, dp, ADMINS
from random import choice


async def echo_message(message: types.Message):
    if message.from_user.id not in ADMINS:

        if message.text.lower() == 'game':
            a = ['⚽️', '🎰', '🏀', '🎯', '🎳', '🎲']
            random = choice(a)
            await bot.send_dice(message.chat.id, emoji=random)
    else:
        try:
            number = int(message.text)
            result = number ** 2
            await bot.send_message(chat_id=message.from_user.id, text=f'{result}')
        except ValueError:
            await bot.send_message(chat_id=message.from_user.id, text=f'{message.text}')


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_message)
