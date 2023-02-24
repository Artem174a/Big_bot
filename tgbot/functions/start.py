from aiogram.types import Message, Contact
from tgbot.database.DB import Database as Db
from tgbot.keyboards.inline import *
from tgbot.functions.account import *


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


async def user_start(message: Message):
    if Db().user_exist(message.from_user.id) is False:
        Db().add_user(telegram_id=message.from_user.id,
                      name=message.from_user.first_name,
                      username=message.from_user.username)
        await message.answer(f"<b>Привет, {message.from_user.first_name}!"
                             f"Я новый бот который умеет всё!</b>\n\n", reply_markup=InlineKeyboard().get_account())
    else:
        await Account(message=message).get_account()