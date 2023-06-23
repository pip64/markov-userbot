from pyrogram import Client, filters
import markovify
import random

app = Client("my_account")

channels = []

@app.on_message()
async def hello(client, message):
    if message.chat.id in channels:
        if len(message.text) >= 1: 
            file = open(f"{message.chat.id}.txt", "a", encoding="utf-8").write(f"{message.text}\n")
            db = open(f"{message.chat.id}.txt", "r", encoding="utf-8").read()
            text_model = markovify.Text(input_text=db, state_size=1, well_formed=False)
            await message.reply(text_model.make_short_sentence(max_chars=55))
    elif ".['getid'];" in message.text:
        await message.reply(message.chat.id)
        print(message.chat.id)
 
app.run()
