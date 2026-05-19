from telethon import TelegramClient, events
from openai import OpenAI
import os

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
ai = OpenAI(api_key=openai_key)

@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text

    response = ai.chat.completions.create(
        model="gpt-5.5-mini",
        messages=[
            {"role": "user", "content": f"Translate to Uzbek: {text}"}
        ]
    )

    await event.reply(response.choices[0].message.content)

client.run_until_disconnected()