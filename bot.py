#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

#원래 코드 그룹-그룹
#@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
#모든 메시지에 응답하기
$@BotzHubUser.on(events.NewMessage(incoming=True))
#특정 유저 메시지에만 반응
@BotzHubUser.on(events.NewMessage(incoming=True, from_users='hoyduly' ))
async def sender_bH(event):
        try:
            #chat = await event.get_chat()
            #print(chat)
            
            # 그냥 복사 붙여넣기 전송
            #await BotzHubUser.send_message(
            #    'duhwan_bot',
            #    event.message
            #)
            
            # 포워딩으로 보내기
            await BotzHubUser.forward_messages('duhwan_bot', event.message)
            
        except Exception as e:
            print(e)
        
#@BotzHubUser.on(events.NewMessage)
#async def my_event_handler(event):
#    if 'hello' in event.raw_text:
#        chat = await event.get_chat()
#        sender = await event.get_sender()
#        chat_id = event.chat_id
#        sender_id = event.sender_id
#        print(chat)
#        print(sender)
#        print(chat_id)
#        print(sender_id)
#        await event.reply('hi!')

print("Bot has started.")
BotzHubUser.run_until_disconnected()
