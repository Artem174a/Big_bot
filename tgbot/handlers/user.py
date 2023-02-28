from aiogram import Dispatcher
from tgbot.functions.account import *
from tgbot.functions.start import *


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*", content_types=types.ContentType.ANY)
    dp.register_message_handler(dialog, content_types=types.ContentType.ANY)
    dp.register_callback_query_handler(callback_account, lambda call: call.data[len(call.data)-7:] == "account")
    dp.register_callback_query_handler(callback_menu, lambda call: call.data[len(call.data) - 4:] == "menu")
