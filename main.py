from  aiogram import Bot,Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo
import json

bot= Bot('6354377326:AAFwnePBEuiEV3zZP5JRVFEphc1UfcXw6jw')
dp=Dispatcher(bot)
admin='670976831'
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup=types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('открыть веб страницу',web_app=WebAppInfo(url='https://nssensse.github.io/fsdfefsdds/')))
    await message.answer('Привет добро пожаловать в exhausted shop',reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message :types.Message):
    res=json.loads(message.web_app_data.data)
    await bot.send_message(message.admin, f'Streamer: {res["name"]}. Nickname: {res["name2"]}. Telegram: {res["utelegram"]}')


executor.start_polling(dp)