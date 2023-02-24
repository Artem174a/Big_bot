import time
from aiogram.types import Message
from tgbot.database.DB import Database as Db
from tgbot.keyboards.inline import *


async def callback_account(call: types.CallbackQuery):
    if call.data == "get_account":
        await Account(call=call).get_account()
    if call.data == "back_to_account":
        await Account(call=call).back_to_account()


async def callback_menu(call: types.CallbackQuery):
    if call.data == "get_menu":
        await Account(call=call).get_account()
    if call.data == "back_to_menu":
        await Account(call=call).back_to_account()


class Menu:
    def __init__(self, message: Message = None, call: types.CallbackQuery = None):
        if message:
            self.object = message
            self.send_message = message.answer
            self.edit_message_text = message.edit_text
        elif call:
            self.object = call
            self.send_message = call.message.answer
            self.edit_message_text = call.message.edit_text
        self.message = message
        self.call = call
        self.get_user = Db().get_user(self.object.from_user.id)
        self.account_info = f'''
<b>Информация о аккаунте:</b>
<em>Здесь вы можете получить информацию о вашем аккаунте</em>
<b>
📁Доступ
╞ ID: <code>{self.get_user.telegram_id}</code>
╞ Логин: <code>@{self.get_user.username}</code>
╞ Регистрация: <code>{time.strftime('%d.%m.%Y г.', time.gmtime(self.get_user.registration_time))}</code>
╞ Email: <code>{self.get_user.email}</code>
╘ Phone: <code>{self.get_user.phone}</code>

💵 
╞ Подписка: <code>{self.get_user.subscribe_date}</code>
╞ Рефералов: <code>{self.get_user.referrals}</code>
╘ Money: <code>{self.get_user.money}</code>
</b>

'''

    async def get_account(self):
        await self.send_message(text=self.account_info, reply_markup=InlineKeyboard().menu_account())

    async def back_to_account(self):
        await self.edit_message_text(text=self.account_info, reply_markup=InlineKeyboard().menu_account())


class Account:
    def __init__(self, message: Message = None, call: types.CallbackQuery = None):
        if message:
            self.object = message
            self.send_message = message.answer
            self.edit_message_text = message.edit_text
        elif call:
            self.object = call
            self.send_message = call.message.answer
            self.edit_message_text = call.message.edit_text
        self.message = message
        self.call = call
        self.get_user = Db().get_user(self.object.from_user.id)
        self.account_info = f'''
<b>Информация о аккаунте:</b>
<em>Здесь вы можете получить информацию о вашем аккаунте</em>
<b>
📁Доступ
╞ ID: <code>{self.get_user.telegram_id}</code>
╞ Логин: <code>@{self.get_user.username}</code>
╞ Регистрация: <code>{time.strftime('%d.%m.%Y г.', time.gmtime(self.get_user.registration_time))}</code>
╞ Email: <code>{self.get_user.email}</code>
╘ Phone: <code>{self.get_user.phone}</code>
   
💵 
╞ Подписка: <code>{self.get_user.subscribe_date}</code>
╞ Рефералов: <code>{self.get_user.referrals}</code>
╘ Money: <code>{self.get_user.money}</code>
</b>

'''

    async def get_account(self):
        await self.send_message(text=self.account_info, reply_markup=InlineKeyboard().menu_account())

    async def back_to_account(self):
        await self.edit_message_text(text=self.account_info, reply_markup=InlineKeyboard().menu_account())
