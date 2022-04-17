from http import client
from telethon import TelegramClient, events 
from telethon.sessions import StringSession

api_id = 17350549
api_hash = "fa459305ef12234df0539b538fdea574"
session = "1BVtsOHMBu2FhH46cicT6Ype1kzYj5nxE3CiQdj2X7Q6BS0GgwsVUSaCsTdaY18PMlDlP4-Nn481mcNlULYPe5HaC3eBFZ_W3S69KBbomQ-7_UZGUh8cmGs2L7zErfL5wesvM44N85yR3wo3exn79PHHyShaX0MQzjsojLhCe7o1r2W-NWzovAy3R6NPPzGZelTM-W7yEdM0z3Fmf8ZIrEZaMXcPGgFBSOOun8w9TzXE9PM2TbJqt-qYqVlsR9qdnFWitFjyEWJIzU_TzAoLoNj-sXP9ydlCUmiqWuxdz55GaU6ZAnDiTzBE-Yc7BwYA0AyJMYyyeHrxoo2PfwQVXuX7noegp2GQ="

client = TelegramClient(StringSession(session) , api_id , api_hash)

@client.on(events.NewMessage(chats=-1001653029817))
async def handler(event) : 
    chat  = await event.get_chat()
    chat_id = event.chat_id
    print("{}{}".format(chat_id,chat))

    if chat_id == -1001653029817 :
        await client.send_message(-1001683437077 , event.message)
        await client.send_message(-1001796193408 , event.message)
        await client.send_message(-1001762536924 , event.message)

client.start()
client.run_until_disconnected()

# TO_ ="-1001623564020 -156432465456"
# TO = [int(i) for i in TO_.split()]

# for i in