import datetime
from quizzer import Quiz
from config import open_weather_token, BOT_API_TOKEN
from aiogram import Bot, types
import requests
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

quizzes_database = {}  # здесь хранится информация о викторинах
quizzes_owners = {}  # здесь хранятся пары "id викторины <—> id её создателя"

URL = 'https://api.thecatapi.com/v1/images/search'
bot = Bot(token=BOT_API_TOKEN)
#bot = Bot(BOT_API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет!')

@dp.message_handler(commands=['start1'])
async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="Создать викторину",
                                           request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    poll_keyboard.add(types.KeyboardButton(text="Отмена"))
    await message.answer("Нажмите на кнопку ниже и создайте викторину!", reply_markup=poll_keyboard)

# Хэндлер на текстовое сообщение с текстом “Отмена”
@dp.message_handler(lambda message: message.text == "Отмена")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer("Действие отменено. Введите /start, чтобы начать заново.", reply_markup=remove_keyboard)


@dp.message_handler(commands=['картинка'])
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Hello!')

#@dp.message_handler(commands=['картинка'])
#async def send_image(message: types.Message):
 #   await bot.send_photo(chat_id=message.from_user.id, photo='https://mobimg.b-cdn.net/v3/fetch/a8/a825274c3f23c6dc799fb1f1a713a44e.jpeg')

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
          #  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе {city}\nТемпература: {cur_weather}C\nВлажность: {humidity}%\n")


    except:
       # await message.reply('Проверьте название города')
        response = requests.get(URL).json()
        random_cat_url = response[0].get('url') 
        if message.text == 'картинка':
            await bot.send_photo(chat_id=message.from_user.id, photo=random_cat_url)
          #  await bot.send_message(chat_id=message.chat.id, text='Hello!')


if __name__ == '__main__':
    executor.start_polling(dp)