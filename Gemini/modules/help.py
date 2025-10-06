from telethon import events, Button
from Gemini import bot

@bot.on(events.NewMessage(pattern="[!?/]help ?(.*)"))
async def help(event):
    if event.is_group:
       await event.reply("Tag saya lalu ketik apa saja untuk memulai percakapan")
       return

    await event.respond("Silahkan ketik apa saja untuk memulai percakapan!", buttons=(Button.inline("Kembali", data="home")))


@bot.on(events.callbackquery.CallbackQuery(data="help"))
async def chelp(event):
     await event.edit(HELP_TEXT, buttons=(Button.inline("Kembali", data="home")))
