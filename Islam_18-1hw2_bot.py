from aiogram.utils import executor

import logging
from canfig import dp,bot,ADMINS
from handler import clients, extra, callback, admin, fsm_anketa,shedule
from database.bot_db import sql_create


clients.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm(dp)
extra.register_handlers_extra(dp)

async def on_startup(dp):
    await shedule.set_scheduler()
    sql_create()
    await bot.send_message(ADMINS[0], 'Я жив!')
async def on_shutdown(dp):
    await bot.send_message(ADMINS[0], 'пока пока !')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,on_shutdown=on_shutdown)
