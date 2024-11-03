from aiogram import Bot, Dispatcher, types, executor

Token = "your token"

bot = Bot(token=Token)
dp=Dispatcher(bot)

@dp.message_handler(commands=['id'])
async def welcome(message:types.Message):
    await message.answer_sticker("CAACAgEAAxkBAAMeZu-iE_LuRXcpSFghyxL_wFQHLdQAAq8CAAKYVyFEvJTaGRuD96w2BA")
    await message.answer(f"Your id: {message.from_user.id}")

@dp.message_handler(content_types=["sticker"])
async def sticker_handler(message: types.Message):
    sticker_id = message.sticker.file_id
    await message.reply(f'sticker id: {sticker_id}')


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
