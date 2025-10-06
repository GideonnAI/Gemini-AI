import requests, json
from telethon import events
from Gemini import *

async def ask_gemini(prompt, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    response = requests.post(url, json=data)
    result = response.json()
    
    try:
        return result['candidates'][0]['content']['parts'][0]['text']
    except:
        return "Maaf, terjadi error saat memproses permintaan."

async def group_message(event, message_text):
    bot_username = (await bot.get_me()).username
    
    if bot_username and f"@{bot_username}" in message_text:
        clean_message = message_text.replace(f"@{bot_username}", "").strip()
      
        if clean_message in ['?start', '!start', '/start']:
            return False
        
        elif clean_message in ['?help', '!help', '/help']:
            return False
        
        else:
            user_message = event.message.text
            response = ask_gemini(user_message, GEMINI_API_KEY)
            await event.reply(response)
            return True
    
    return False

async def private_message(event, message_text):
    if message_text in ['?start', '!start', '/start']:
        return False
    
    elif message_text in ['?help', '!help', '/help']:
        return False
    
    else:
        user_message = event.message.text
        response = ask_gemini(user_message, GEMINI_API_KEY)
        await event.respond(response)
        return True

@bot.on(events.NewMessage)
async def chat(event):
    if event.sender_id == (await bot.get_me()).id:
        return
    
    chat = await event.get_chat()
    message_text = event.message.text or ""
    
    is_group = hasattr(chat, 'megagroup') or hasattr(chat, 'broadcast')
    
    if is_group:
        await group_message(event, message_text)
    else:
        await private_message(event, message_text)
