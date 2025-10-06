import pytz
from datetime import datetime
from Gemini import bot
from telethon import events, Button


START_TEXT = """
** [{}](tg://user?id={})!**

**I'm Gemini AI Chatbot.**

**Klik tombol di bawah ini untuk menu bantuan!**
"""


START_BTN = [
                [
                    Button.inline("Bantuan", data="help"),
                    Button.url("Situs", "https://gemini.google.com/?hl=id")
                ]
            ]

async def selamat():
    wib_tz = pytz.timezone('Asia/Jakarta')
    wib_time = datetime.now(wib_tz)
    jam = int(wib_time.strftime('%H'))
    
    if 0 <= jam < 5:
        return f"Selamat dini hari!"
    elif 5 <= jam < 12:
        return f"Selamat pagi!"
    elif 12 <= jam < 15:
        return f"Selamat siang!️"
    elif 15 <= jam < 19:
        return f"Selamat sore!"
    elif 19 <= jam < 24:
        return f"Selamat malam!"
    else:
        return "Selamat datang!"
        

@bot.on(events.NewMessage(pattern="^[?!/]start ?(.*)"))
async def start(event):
    salam = await selamat()

    if event.is_private:
       await event.respond(selamat() + START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN
       )
       return

    if event.is_group:
       await event.reply(salam + " Ada yang bisa saya bantu hari ini?",
        buttons=
        [
            Button.url("Website", "https://gemini.google.com")
        ]
       )
       return


@bot.on(events.callbackquery.CallbackQuery(data="home"))
async def hstart(event):
     salam = await selamat()
     await event.edit(salam + START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN)
