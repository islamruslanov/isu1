# from aiogram import types,Bot,Dispatcher
# from aiogram.utils import executor
# from decouple import config
# import logging
# from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
#
# TOKEN = config('TOKEN')
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot=bot)
#
#
# @dp.message_handler(commands=['quiz'])
# async def quiz1(message: types.Message):
#     markup = InlineKeyboardMarkup()
#     button1 = InlineKeyboardButton("next",callback_data='quiz_1_button')
#     markup.add(button1)
#     question ='Столица Греции?'
#     answer = [
#         'Оттава',
#         "Берлин ",
#         "Сеул",
#         "Афины"
#     ]
#     await bot.send_poll(
#         chat_id=message.from_user.id,
#         question=question,
#         options=answer,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=3,
#         reply_markup=markup,
#     )
# @dp.callback_query_handler(text="quiz_1_button")
# async def quiz_2(cull: types.CallbackQuery):
#     question = 'Столица Канады'
#     answer = [
#         'Оттава',
#         "Канберра",
#         "Вена",
#         "Мехико,"
#     ]
#     await bot.send_poll(
#         chat_id=cull.from_user.id,
#         question=question,
#         options=answer,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=1
#
#     )
#
# @dp.message_handler(commands=['mem'])
# async def mem_image(message: types.Message):
#     await bot.send_photo(chat_id=message.from_user.id,photo='https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.tildacdn.com%2Ftild6465-6132-4937-b964-336163313261%2Fmem-2-1024x683.jpg&tbnid=1vONJoAIIF36gM&vet=12ahUKEwioyp7np5_-AhVFtioKHfr6A5AQMygBegUIARC3AQ..i&imgrefurl=https%3A%2F%2Fbiplane.ru%2Fblog%2Fchto-takoe-mem-i-kak-ego-ispolzovat-v-obshhenii-s-klientami%2F&docid=X_vvWeMf08qBdM&w=1024&h=683&q=mem&ved=2ahUKEwioyp7np5_-AhVFtioKHfr6A5AQMygBegUIARC3AQ')
#
#
#
# @dp.message_handler()
# async def echo_message(message):
#     try:
#         number = int(message.text)
#         result = number ** 2
#         await bot.send_message(chat_id=message.from_user.id, text=f'{result}')
#     except ValueError:
#         await bot.send_message(chat_id=message.from_user.id, text=f'{message.text}')
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     executor.start_polling(dp, skip_updates=True)
