import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from database.bot_db import sql_command_all_users
from canfig import bot


async def juma_mubarak(bot: Bot):
    users = await sql_command_all_users()
    for user in users:
        await bot.send_message(user[0], f'{user[-1]} Джума мубарак!')


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    scheduler.add_job(
        juma_mubarak,
        kwargs={'bot': bot},
        trigger=IntervalTrigger(
            weeks=1,
            days=1,
            hours=8,
            start_date=datetime.datetime.now()
        )
    )
    scheduler.start()
