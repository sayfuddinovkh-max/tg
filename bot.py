from telethon import TelegramClient, events
from openai import OpenAI
import os

api_id = 12345678
api_hash = "API_HASHING"
bot_token = "BOT_TOKENING"
openai_key = "OPENAI_API_KEYING"

client = TelegramClient('bot', api_id, api_hash)
ai = OpenAI(api_key=openai_key)

@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text

    response = ai.chat.completions.create(
        model="gpt-5.5-mini",
        messages=[
            {
                "role": "user",
                "content": f"Translate this text to English: {text}"
            }
        ]
    )

    answer = response.choices[0].message.content

    await event.reply(answer)

print("BOT STARTED")

client.start(bot_token=bot_token)
client.run_until_disconnected()