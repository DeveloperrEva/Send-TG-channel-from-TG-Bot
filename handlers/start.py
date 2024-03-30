from main import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from state import channel, add
from data import db

@dp.message_handler(commands=['send'])
async def process_start_command(message: types.Message, state="*"):
    await state.finish()
    await message.answer("Отправьте мне текст")
    await channel.send.set()
    
@dp.message_handler(state=channel.send, content_types=['text'])
async def process_messages(message: types.Message, state: FSMContext):
    text = message.text

    rows = db.select()
    
    for row in rows:
        channel_id = row[0]

        await bot.send_message(chat_id=channel_id, text=text)
        await message.answer("Успешно отправлено")
    await state.finish()

@dp.message_handler(commands=['add'])
async def process_start_command(message: types.Message, state="*"):
    await state.finish()
    await message.answer("Отправьте мне ID канала")
    await add.chan.set()
    
@dp.message_handler(state=add.chan, content_types=['text'])
async def process_messages(message: types.Message, state: FSMContext):
    text = message.text

    db.add(text)
    await message.answer("Успешно отправлено")
    await state.finish()