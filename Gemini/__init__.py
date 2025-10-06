import os, logging
from dotenv import load_dotenv
from telethon import TelegramClient

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

load_dotenv()

TOKEN = os.getenv("TOKEN", None)

bot = TelegramClient(
        "tgbot",
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        ).start(bot_token=TOKEN)
