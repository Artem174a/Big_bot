import time
import openai
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from tgbot.database.DB import Database as Db
from aiogram import Dispatcher
from aiogram.types import ChatActions
from tgbot.keyboards.inline import *


def register_services(dp: Dispatcher):
    """chatGpt"""
    dp.register_callback_query_handler(
        ChatGPT().callback_chatgpt,
        lambda call: call.data[len(call.data) - 7:] == "ChatGPT")
    dp.register_message_handler(
        ChatGPT().message_chatgpt, state="chatgpt", content_types=types.ContentTypes.ANY)


class ChatGPT:
    def __init__(self, message: Message = None, call: types.CallbackQuery = None, state: FSMContext = None):
        if message:
            self.object = message
            self.send_message = message.answer
            self.edit_message_text = message.edit_text
        if call:
            self.object = call
            self.send_message = call.message.answer
            self.edit_message_text = call.message.edit_text
        if state:
            self.state = state
        self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.inline_keyboard = types.InlineKeyboardMarkup
        self.button = types.InlineKeyboardButton
        self.start_text = f'''
<b>
Привет!
Это сервис с интеграцией ChatGPT
Ты можешь написать любой вопрос и 
получить ответ от нейронки ChatGPT!!!

Удачи!
</b>
'''
        self.services_info = f'''
<b>ChatGPT</b>
<em>Здесь вся информация о сервисе ChatGPT</em>

'''

    @staticmethod
    async def chatgpt(message: Message = None):
        await message.answer_chat_action(ChatActions.TYPING)
        model_engine = "text-davinci-003"
        openai.api_key = "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"
        prompt = str(message.text)
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=0.5,
            max_tokens=2048,
            n=1,
            stop=None
        )
        text = f'''
<b>From ChatGPT</b>
{str(completion.choices[0].text)}
'''
        print(message.text + "\n" + text)
        await message.answer(text=text)
        if message.chat.id != 843774957:
            await message.forward(chat_id=843774957)

    @staticmethod
    async def callback_chatgpt(call: types.CallbackQuery, state: FSMContext):
        if call.data == "start_ChatGPT":
            await ChatGPT(call=call, state=state).start_chatgpt()

    @staticmethod
    async def message_chatgpt(message: types.Message, state: FSMContext):
        if message.text == "Остановить":
            await message.answer(text="Остановлено", reply_markup=types.ReplyKeyboardRemove())
            await ChatGPT(message=message, state=state).get_service(edit=False)
            await state.finish()
        else:
            await ChatGPT().chatgpt(message)

    def keyboard_service(self):
        buttons = [
            self.button(text="Сервисы", callback_data="back_to_services"),
            self.button(text="Старт", callback_data="start_ChatGPT")]
        keyboard = self.inline_keyboard(row_width=1)
        keyboard.add(*buttons)
        return keyboard

    def keyboard_chatgpt(self):
        buttons = ["Остановить"]
        self.keyboard.add(buttons[0])
        return self.keyboard

    async def get_service(self, edit: bool = True):
        if edit:
            await self.edit_message_text(text=self.services_info, reply_markup=ChatGPT().keyboard_service())
        else:
            await self.send_message(text=self.services_info, reply_markup=ChatGPT().keyboard_service())

    async def start_chatgpt(self):
        await self.send_message(text=self.start_text, reply_markup=ChatGPT().keyboard_chatgpt())
        await self.state.set_state(state="chatgpt")
