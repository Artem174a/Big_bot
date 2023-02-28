from aiogram.types import Message, Contact
from tgbot.database.DB import Database as Db
from tgbot.keyboards.inline import *
from aiogram.types import ChatActions
from tgbot.functions.account import *
import openai


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


async def user_start(message: Message):
    if Db().user_exist(message.from_user.id) is False:
        Db().add_user(telegram_id=message.from_user.id,
                      name=message.from_user.first_name,
                      username=message.from_user.username)
        await message.answer(f'''
<b>Привет, {message.from_user.first_name}!</b>
Это новый бот который позволяет 
пользоваться большим колличеством сервисов!
        ''', reply_markup=InlineKeyboard().start())
    else:
        await message.answer(f'''
<b>Привет, {message.from_user.first_name}!</b>
Мы снова рады тебя видеть!
        ''', reply_markup=InlineKeyboard().start())

