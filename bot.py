from telethon import TelegramClient, events
from openai import OpenAI
import os

# ENV
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
groq_key = os.getenv("GROQ_API_KEY")

# TELEGRAM
client = TelegramClient("bot", api_id, api_hash)

# GROQ
ai = OpenAI(
    api_key=groq_key,
    base_url="https://api.groq.com/openai/v1"
)

print("GROQ TRANSLATOR STARTED")

@client.on(events.NewMessage)
async def handler(event):
    try:
        text = event.raw_text

        if event.out:
            return

        response = ai.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional English to Uzbek translator. "
                        "Translate naturally into Uzbek."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        answer = response.choices[0].message.content

        await event.reply(answer)

    except Exception as e:
        await event.reply(f"ERROR: {e}")

client.start(bot_token=bot_token)
client.run_until_disconnected()