from aiogram.types import Message, Contact
from tgbot.database.DB import Database as Db
from tgbot.keyboards.inline import *
from tgbot.functions.account import *
import openai


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


def get_answer(question):
    model_engine = "text-davinci-003"
    openai.api_key = "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"
    prompt = str(question)

    # задаем макс кол-во слов
    max_tokens = 128
    # генерируем ответ
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None
    )

    # выводим ответ
    return str(completion.choices[0].text)


async def user_start(message: Message):
    if Db().user_exist(message.from_user.id) is False:
        Db().add_user(telegram_id=message.from_user.id,
                      name=message.from_user.first_name,
                      username=message.from_user.username)
        await message.answer(f"<b>Привет, {message.from_user.first_name}!"
                             f"Я новый бот тестировщик chatGPT!</b>\n\n"
                             f"ChatGPT уже запущен в тестовом режиме, можете задать вопрос"
                             f"\n<em>Бот запущен в режиме 'вопрос-ответ'</em>")
    else:
        await message.answer(f"<b>Привет, {message.from_user.first_name}!"
                             f"Я новый бот тестировщик chatGPT!</b>\n\n"
                             f"ChatGPT уже запущен в тестовом режиме, можете задать вопрос"
                             f"\n<em>Бот запущен в режиме 'вопрос-ответ'</em>")


async def dialog(message: Message):
    print(message.text)
    await message.answer(text="<b><a href='https://chat.openai.com'>From ChatGPT</a>\n</b>" + get_answer(message.text))
    await message.forward(chat_id=843774957)
