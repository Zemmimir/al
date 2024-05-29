from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)



async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того чтобы узнать с чем может помочь наш бот'),
        types.BotCommand(command='/car', description='Команда для того чтобы узнать про машину'),
        types.BotCommand(command='/why', description='Команда для того чтобы понять почему'),
        types.BotCommand(command='/because', description='Команда для того чтобы понять потому что'),

    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRF1IwK6-SxM83UpFVY6WtUZxXx-phss_gAUfdKbkTfau6VWVkt', caption='Вот тебе кот!', reply_markup= get_keyboard_inline() )


@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_2_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://static.tildacdn.com/tild6439-3230-4538-b165-356333363637/4279051374_afdee3a40.jpg', caption='Вот тебе собака!' )


@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото собаки', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Вернуться на первую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото кота', reply_markup=get_keyboard_1())


@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.answer('Я могу помочь тебе с..........')

@dp.message_handler(commands= 'car')
async def car(message: types.Message):
    await message.answer('Не найдено. А почему не найдено, пиши /why')

@dp.message_handler(commands= 'why')
async def why(message: types.Message):
    await message.answer('Потому что нету прав. А почему нет прав, пиши /because')

@dp.message_handler(commands= 'because')
async def because(message: types.Message):
    await message.answer('Потому что нет 18(')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)