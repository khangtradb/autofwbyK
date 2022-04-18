from http import client
from telethon import TelegramClient, events 
from telethon.sessions import StringSession

api_id = 17350549
api_hash = "fa459305ef12234df0539b538fdea574"
session = "1BVtsOHYBu6AVGNeG32J58rbqKFpAAY0hu4MqLaMUEngS-GEIlUN2JnRh-s8BKRUTmlSB3teIrfWDiLHQkxL8IZwzQtDnrIusQlXafLzNfhLxmVgfcZ-JlSehaZ1FKkA6bhU0tBBc3saG0L0inMx3y6euuKUYUCHV4ns0jAM4J8jfn_Q7GSmIYXep_7zGJgDBPrMCMGTik-Zgyr-dkJbfRIKwcQTZbTe3BDXwioiTYlvoP6CjyktdBFmBeWc6Aw9bgtb8WTmTnSBdC3snyyBBcgTpSt_hoRoDaBa8YpdNgQA27oP8HvH9Nj5dxOJZXQgEXFuZ8hIFupM2kRY4ZAFncfTXH-tjqCU="

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