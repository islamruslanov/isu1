from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from canfig import ADMINS
from handler.client_kb import cancel_markup,submit_markup
from database.bot_db import sql_command_insert



class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:  # Закреплять сообщения могут только админы
        await message.answer('Ты не админ!')
    else:
        await FSMAdmin.id.set()
        await message.answer('telegram_id ментора:',reply_markup=cancel_markup)


async def laod_id(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['telegram_id'] = message.text
    await FSMAdmin.next()
    await message.answer('Имя ментора?')


async def laod_name(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Напрвление ментора?')


async def laod_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Возраст ментора: ')


async def laod_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("пиши число")
    elif 16 > int(message.text) < 60:
        await message.answer('Возрастное ограничение!')
    else:
        async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
            FSMCONTEXT_PROXY_STORAGE['age'] = message.text
        await FSMAdmin.next()
        await message.answer('группа ментора: ')


async def laod_group(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['group'] = message.text
        await message.answer(
            f'id ментора: {FSMCONTEXT_PROXY_STORAGE["telegram_id"]} \n '
            f'Имя ментора: {FSMCONTEXT_PROXY_STORAGE["name"]} \n'
            f'Направление ментора:{FSMCONTEXT_PROXY_STORAGE["direction"]} \n'
            f'Возратс ментора: {FSMCONTEXT_PROXY_STORAGE["age"]}\n'
            f'группа ментора {FSMCONTEXT_PROXY_STORAGE["group"]} '
        )
    await FSMAdmin.next()
    await message.answer('Все верно?',reply_markup=submit_markup)


async def sumbit_state(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer('все свободен ')
    if message.text.lower() == 'заново':
        await FSMAdmin.id.set()
        await message.answer('telegram_id ментора')

async def cancel_reg(message: types.Message,state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer('Ну и пошел ты')



def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_reg,state='*',commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(cancel_reg, Text(equals='отмена', ignore_case=True),state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(laod_id, state=FSMAdmin.id)
    dp.register_message_handler(laod_name, state=FSMAdmin.name)
    dp.register_message_handler(laod_direction, state=FSMAdmin.direction)
    dp.register_message_handler(laod_age, state=FSMAdmin.age)
    dp.register_message_handler(laod_group, state=FSMAdmin.group)
    dp.register_message_handler(sumbit_state, state=FSMAdmin.submit)
