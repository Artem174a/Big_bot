from aiogram import types


class InlineKeyboard:
    def __init__(self):
        self.inline_keyboard = types.InlineKeyboardMarkup
        self.button = types.InlineKeyboardButton
        pass

    def get_account(self):
        buttons = [
            types.InlineKeyboardButton(text="Мой аккаунт 💼 ", callback_data="get_account")]
        keyboard = self.inline_keyboard(row_width=1)
        keyboard.add(*buttons)
        return keyboard

    def menu_account(self):
        buttons = [
            self.button(text="Подписка", callback_data="back_to_account"),
            self.button(text="Инфо", callback_data="back_to_account"),
            self.button(text="Поддержка", callback_data="back_to_account"),
            self.button(text="Меню", callback_data="get_menu"),
        ]
        keyboard = self.inline_keyboard()
        keyboard.add(buttons[0])
        keyboard.add(buttons[1], buttons[2])
        keyboard.add(buttons[3])
        return keyboard
