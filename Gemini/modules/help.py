from telethon import events, Button
from Gemini import bot

bot_username = bot.get_me().username
HELP_TEXT = f"""
Di Grup: Tag saya lalu ketik apa saja untuk memulai percakapan
Contoh: @{bot_username} Apa itu AI?

Chat Pribadi: Silahkan ketik apa saja untuk memulai percakapan!
"""

@bot.on(events.NewMessage(pattern="[!?/]help ?(.*)"))
async def help(event):
    if event.is_group:
       await event.reply(HELP_TEXT)
       return

    await event.respond(HELP_TEXT, buttons=(Button.inline("Kembali", data="home")))


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def chelp(event):
     await event.edit(HELP_TEXT, buttons=(Button.inline("Kembali", data="home")))
