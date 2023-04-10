from aiogram import Dispatcher,types
from canfig import bot,ADMINS


async def pin_handlers(message: types.Message):
    if message.chat.type !='private':
        if message.from_user.id not  in ADMINS:
            await message.answer('Ты не админ! ')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на собшение!')
        else:
            await bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.message_id)

    else:
        await message.answer('пиши в группе!')


def register_handlers_admin(dp:Dispatcher):
    dp.register_message_handler(pin_handlers,commands=['pin'],commands_prefix="!/")






