import aiogram
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType
from aiogram.utils.executor import start_polling

# Инициализируем бота
bot = aiogram.Bot(token="<YOUR_BOT_TOKEN>")

# Инициализируем диспетчер
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработчик команды start
@dp.message_handler(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот с интеграцией chatGPT. Что ты хочешь спросить?")

# Обработчик текстовых сообщений
@dp.message_handler(content_types=ContentType.TEXT)
async def echo_message(message: Message):
    # Здесь интегрируем chatGPT
    await message.answer("Ответ от chatGPT")

# Запускаем прослушивание обновлений
start_polling(dp)