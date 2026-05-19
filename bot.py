from telethon import TelegramClient, events
from groq import Groq
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
groq_key = os.getenv("GROQ_API_KEY")

client = TelegramClient('bot', api_id, api_hash)
ai = Groq(api_key=groq_key)

@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text

    try:
        response = ai.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"Translate this text to Uzbek: {text}"
                }
            ]
        )

        answer = response.choices[0].message.content
        await event.reply(answer)

    except Exception as e:
        await event.reply(f"ERROR: {e}")

print("BOT STARTED")

client.start(bot_token=bot_token)
client.run_until_disconnected()