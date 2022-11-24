"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()




API_TOKEN = os.environ["BOT_TOKEN"]

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
print(f"BOT_TOKEN: {API_TOKEN}")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    print(f"message.from_user: {message.from_user}")
    print(f"message.text: {message.text}")
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    print(f"message.from_user: {message.from_user}")
    print(f"message.text: {message.text}")
    print(f"message.message_id: {message.message_id}")
    print(f"message.date: {message.date}")
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
