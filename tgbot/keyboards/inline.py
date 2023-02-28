from aiogram import types


class InlineKeyboard:
    def __init__(self):
        self.inline_keyboard = types.InlineKeyboardMarkup
        self.button = types.InlineKeyboardButton
        pass

    def start(self):
        buttons = [
            self.button(text="Мой аккаунт 💼 ", callback_data="back_to_account"),
            self.button(text="Меню", callback_data="back_to_menu")]
        keyboard = self.inline_keyboard(row_width=1)
        keyboard.add(*buttons)
        return keyboard

    def menu(self):
        buttons = [
            self.button(text="Мой аккаунт 💼 ", callback_data="back_to_account"),
            self.button(text="Сервисы", callback_data="back_to_services")]
        keyboard = self.inline_keyboard(row_width=1)
        keyboard.add(*buttons)
        return keyboard

    def account_menu(self):
        buttons = [
            self.button(text="Подписка", callback_data="subscribe_account"),
            self.button(text="Инфо", callback_data="info_account"),
            self.button(text="Поддержка", callback_data="support_account"),
            self.button(text="Меню", callback_data="back_to_menu"),
        ]
        keyboard = self.inline_keyboard()
        keyboard.add(buttons[0])
        keyboard.add(buttons[1], buttons[2])
        keyboard.add(buttons[3])
        return keyboard

    def services(self):
        buttons = [
            self.button(text="ChatGPT", callback_data="ChatGPT_serv"),
            self.button(text="Меню", callback_data="back_to_menu")]
        keyboard = self.inline_keyboard(row_width=1)
        keyboard.add(*buttons)
        return keyboard
