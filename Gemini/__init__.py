import os, logging
from telethon import TelegramClient

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

TOKEN = os.environ.get("TOKEN", None)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", None)

bot = TelegramClient(
        "tgbot",
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        ).start(bot_token=TOKEN)
