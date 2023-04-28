from aiogram import Dispatcher,types
from canfig import bot,dp
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from database.bot_db import sql_command_random,sql_command_all_users,sql_command_insert_user
from .utils import get_ids_from_users

# @dp.message_handler(commands=['quiz'])



async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("next", callback_data='quiz_1_button')
    markup.add(button)
    question = 'Столица Греции?'
    answer = [
        'Оттава',
        "Берлин ",
        "Сеул",
        "Афины"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        reply_markup=markup,
    )




# @dp.message_handler(commands=['mem'])
async def mem_image(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.tildacdn.com%2Ftild6465-6132-4937-b964-336163313261%2Fmem-2-1024x683.jpg&tbnid=1vONJoAIIF36gM&vet=12ahUKEwioyp7np5_-AhVFtioKHfr6A5AQMygBegUIARC3AQ..i&imgrefurl=https%3A%2F%2Fbiplane.ru%2Fblog%2Fchto-takoe-mem-i-kak-ego-ispolzovat-v-obshhenii-s-klientami%2F&docid=X_vvWeMf08qBdM&w=1024&h=683&q=mem&ved=2ahUKEwioyp7np5_-AhVFtioKHfr6A5AQMygBegUIARC3AQ')
async def start_comands(message:types.Message):
    users = await sql_command_all_users()
    ids = get_ids_from_users(users)
    if message.from_user.id not in ids:
        await sql_command_insert_user(
            message.from_user.id,
            message.from_user.username,
            message.from_user.full_name
        )
    await message.reply('чем вам могу памочь')


async def get_random_anketa(message: types.Message):
    random_user = await sql_command_random()
    await message.answer(
        f'id ментора: {random_user[1]} \n '
        f'Имя ментора: {random_user[2]} \n'
        f'Направление ментора:{random_user[3]} \n'
        f'Возратс ментора: {random_user[4]}\n'
        f'группа ментора {random_user[5]}'
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(mem_image,commands=['mem'])
    dp.register_message_handler(quiz1,commands=['quiz'])
    dp.register_message_handler(start_comands,commands=['start'])
    dp.register_message_handler(get_random_anketa,commands=['get'])

