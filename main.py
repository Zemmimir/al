from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN

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
    await message.answer('Привет, я твой первый ЭХО бот')

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