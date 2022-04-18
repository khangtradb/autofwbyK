from http import client
from telethon import TelegramClient, events 
from telethon.sessions import StringSession

api_id = 17350549
api_hash = "fa459305ef12234df0539b538fdea574"
session = "1BVtsOGYBuyWNqaCMbg_i0h9Xri87QtK5bU1nNuQT5pGzXBPAWS1crqIg4njb2y-Bb7BT3IRj_Xie7cTL760132JUl8eKFqqX9rm_NswXcWS_OQIriyr_OMV7nLLZ3n4sG-fA4XNCRIDI0IOgBf6ZMztvyc422-ss0o2rfPcBZ01lVSecq9oyXGV2uQ8iu7uqJZh0PyjVJPrGEnCiaS7Iqf_K-ieqvbafl6clf6ekaACTtQO7KEOQWjaLtUOEQkDif2oJJhUZC0GzVF7Mc2aRV8N-eD-bfSiDynAJq9DHexyFgYTmIY0KxapqA0qTlcKivFiPEp1uPgBBZ3Gui4zyT7PAwFJdwUs="

client = TelegramClient(StringSession(session) , api_id , api_hash)

@client.on(events.NewMessage(chats=-1001709343473))
async def handler(event) : 
    chat  = await event.get_chat()
    chat_id = event.chat_id
    print("{}{}".format(chat_id,chat))

    if chat_id == -1001709343473 :
        await client.send_message(-1001683437077 , event.message)
        await client.send_message(-1001796193408 , event.message)
        await client.send_message(-1001762536924 , event.message)

client.start()
client.run_until_disconnected()

# TO_ ="-1001623564020 -156432465456"
# TO = [int(i) for i in TO_.split()]

# for i in