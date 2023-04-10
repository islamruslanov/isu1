from aiogram import Dispatcher,types
from canfig import bot,dp
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


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
async def help_comands(message:types.Message):
    await message.reply('чем вам могу памочь')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(mem_image,commands=['mem'])
    dp.register_message_handler(quiz1,commands=['quiz'])
    dp.register_message_handler(help_comands,commands=['help'])

