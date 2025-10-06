from telethon import events
import google.generativeai as genai
from Gemini import bot, GEMINI_API_KEY

model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key=GEMINI_API_KEY)

async def group_message(event, message_text):
    chat = await event.get_chat()
    message_txt = event.message.text
    response = model.generate_content(message)
    bot_username = (await bot.get_me()).username
    
    if bot_username and f"@{bot_username}" in message_text:
        clean_message = message_text.replace(f"@{bot_username}", "").strip()
      
        if clean_message in ['?start', '!start', '/start']:
            return False
        
        elif clean_message in ['?help', '!help', '/help']:
            return False
        
        else:
            await event.reply(response.text)
            return True
    
    return False

async def private_message(event, message_text):
    chat = await event.get_chat()
    message_txt = event.message.text
    response = model.generate_content(message)
  
    if message_text in ['?start', '!start', '/start']:
        return False
    
    elif message_text in ['?help', '!help', '/help']:
        return False
    
    else:
        await event.respond(response.text)
        return True

@bot.on(events.NewMessage)
async def chat(event):
    if event.sender_id == (await client.get_me()).id:
        return
    
    chat = await event.get_chat()
    message_text = event.message.text or ""
    
    is_group = hasattr(chat, 'megagroup') or hasattr(chat, 'broadcast')
    
    if is_group:
        await group_message(event, message_text)
    else:
        await private_message(event, message_text)
