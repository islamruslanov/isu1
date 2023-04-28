from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from canfig import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete


async def pin_handlers(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не админ! ')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на собшение!')
        else:
            await bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.message_id)

    else:
        await message.answer('пиши в группе!')


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('ты не админ ')
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer(
                f'id ментора: {user[1]} \n '
                f'Имя ментора: {user[2]} \n'
                f'Направление ментора:{user[3]} \n'
                f'Возратс ментора: {user[4]}\n'
                f'группа ментора {user[5]}',
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(
                        F'DELETE {user[2]}',
                        callback_data=f'delete {user[0]} '
                    )
                )

            )


async def complete_delete(call: types.CallbackQuery):
    user_id = sql_command_delete(call.data.replace('delete',''))
    await sql_command_delete(user_id)
    await call.answer(text=f'удален запись с айди:{user_id}',
                      show_alert=True )



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin_handlers, commands=['pin'], commands_prefix="!/")
    dp.register_message_handler(delete_data, commands=['delete'])
    dp.register_callback_query_handler(complete_delete,lambda call: call.data and call.data.startswith('delete '))



