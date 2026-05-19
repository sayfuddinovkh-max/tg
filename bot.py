from telethon import TelegramClient, events
from groq import Groq
import os

# API
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
groq_key = os.getenv("GROQ_API_KEY")

# TELEGRAM CLIENT
client = TelegramClient("session", api_id, api_hash)

# GROQ AI
ai = Groq(api_key=groq_key)

# SOURCE CHANNEL
SOURCE_CHANNEL = "xebpi"

# TARGET CHANNEL
TARGET_CHANNEL = "tezkoryangiliklar6"

print("AUTO TRANSLATOR STARTED")

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        text = event.raw_text

        if not text:
            return

        response = ai.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an elite English-to-Uzbek translator.

Rules:
- Translate naturally like real Uzbek news channels.
- Do NOT translate word-by-word.
- Make it fluent and easy to read.
- Keep emojis and formatting.
- ONLY output Uzbek translation.
- No explanations.
- No original English text.
"""
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        translated = response.choices[0].message.content.strip()

        # SEND TO YOUR CHANNEL
        await client.send_message(TARGET_CHANNEL, translated)

        print("POST SENT")

    except Exception as e:
        print("ERROR:", e)

print("BOT RUNNING...")

client.start()
client.run_until_disconnected()