from Gemini import bot
from Gemini.modules import *
from telethon import events, Button


START_TEXT = """
**Hi [{}](tg://user?id={})!**

**I'm Gemini AI Chatbot.**

**Klik tombol di bawah ini untuk menu bantuan!**
"""


START_BTN = [
                [
                    Button.url("Bantuan", data="help"),
                    Button.url("Situs", "https://gemini.google.com/?hl=id")
                ]
            ]


@bot.on(events.NewMessage(pattern="^[?!/]start ?(.*)"))
async def start(event):

    if event.is_private:
       await event.respond(START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN
       )
       return

    if event.is_group:
       await event.reply("**Halo! Ada yang bisa saya bantu hari ini?**",
        buttons=
        [
            Button.url("Website", "https://gemini.google.com")
        ]
       )
       return


@bot.on(events.callbackquery.CallbackQuery(data="home"))
async def hstart(event):
     await event.edit(START_TEXT.format(event.sender.first_name, event.sender_id), buttons=START_BTN)
