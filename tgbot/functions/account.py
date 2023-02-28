import time

from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.database.DB import Database as Db
from tgbot.keyboards.inline import *
from tgbot.functions.services import *


async def callback_account(call: types.CallbackQuery):
    if call.data == "get_account":
        await Account(call=call).get_account()
    if call.data == "back_to_account":
        await Account(call=call).back_to_account()
    if call.data == "subscribe_account":
        await Account(call=call).subscribe_account()
    if call.data == "info_account":
        await Account(call=call).info_account()
    if call.data == "support_account":
        await Account(call=call).support_account()


async def callback_menu(call: types.CallbackQuery):
    if call.data == "get_menu":
        await Menu(call=call).get_menu()
    if call.data == "back_to_menu":
        await Menu(call=call).back_to_menu()


async def callback_services(call: types.CallbackQuery, dp: Dispatcher = None):
    if call.data == "get_services":
        await Services(call=call).get_services()
    if call.data == "back_to_services":
        await Services(call=call).back_to_services()
    if call.data[len(call.data) - 4:] == "serv":
        print(call.data[:len(call.data) - 5])
        await eval(f"{call.data[:len(call.data) - 5]}(call=call).get_service()")


class Services:
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
        self.services_info = f'''
<b>Сервисы</b>
<em>Здесь вы сможете найти нужный вам сервис</em>
<b>

Действующие сервисы:
╘ <em>Прототип ChatGPT</em>
</b>

'''

    async def get_services(self):
        await self.send_message(text=self.services_info, reply_markup=InlineKeyboard().services())

    async def back_to_services(self):
        await self.edit_message_text(text=self.services_info, reply_markup=InlineKeyboard().services())


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
        self.menu_info = f'''
<b>Меню</b>
<em>Основное о чат-боте</em>
<b>
Основное меню в разработке!

Действующие сервисы:
╘ <em>Прототип ChatGPT</em>
</b>

'''

    async def get_menu(self):
        await self.send_message(text=self.menu_info, reply_markup=InlineKeyboard().menu())

    async def back_to_menu(self):
        await self.edit_message_text(text=self.menu_info, reply_markup=InlineKeyboard().menu())


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
        self.subscribe_info = "Пока недоступно"
        self.info_info = "Пока недоступно"
        self.support_info = "Пока недоступно"

    async def get_account(self):
        await self.send_message(text=self.account_info, reply_markup=InlineKeyboard().account_menu())

    async def back_to_account(self):
        await self.edit_message_text(text=self.account_info, reply_markup=InlineKeyboard().account_menu())

    async def subscribe_account(self):
        await self.call.answer(text=self.subscribe_info)

    async def info_account(self):
        await self.call.answer(text=self.info_info)

    async def support_account(self):
        await self.call.answer(text=self.subscribe_info)
