from telethon import TelegramClient, events
from openai import OpenAI
import os

# ENV
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]
openai_key = os.environ["OPENAI_API_KEY"]

# CLIENTS
client = TelegramClient("bot", api_id, api_hash)
ai = OpenAI(api_key=openai_key)

# MESSAGE HANDLER
@client.on(events.NewMessage)
async def handler(event):
    try:
        text = event.raw_text

        response = ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful translator."
                },
                {
                    "role": "user",
                    "content": f"Translate this text to English:\n\n{text}"
                }
            ]
        )

        answer = response.choices[0].message.content

        await event.reply(answer)

    except Exception as e:
        await event.reply(f"Error: {e}")

print("BOT STARTED")

client.start(bot_token=bot_token)
client.run_until_disconnected()