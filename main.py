from  aiogram import Bot,Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo
import json

bot= Bot('6366181128:AAG0d8Cxz-JraiVd4_dqHk8vhEe6jHEmhLQ')
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup=types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('открыть веб страницу',web_app=WebAppInfo(url='https://nssensse.github.io/dfjdsjsdkeufu/')))
    await message.answer('Привет добро пожаловать в exhausted shop',reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message :types.Message):
    res=json.loads(message.web_app_data.data)
    await message.answer(f'Streamer: {res["name"]}. Nickname: {res["name2"]}. Telegram: {res["utelegram"]}')


executor.start_polling(dp)