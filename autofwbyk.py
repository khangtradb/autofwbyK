from http import client
from telethon import TelegramClient, events 
from telethon.sessions import StringSession

api_id = 17350549
api_hash = "fa459305ef12234df0539b538fdea574"
session = "1BVtsOHYBu0CSQ-aAGCy-_pPjx8yBKpytWtLWp6QYZ1f3-xiizvAWL6wTuaX5WeozxRnhkbYwGnyMVOeiVsI89hsorkUNYa_4zy4vZQ-iabWpwNaIIBzp1pZ3sMAXq7nRHCrD8yvihR2aT6yb-I_qFI2zGnHHBtI7oFiuLtjgHFu9YuBNF1TB3blOVp2ihQvpTb4323dpRzYA2ck3kseVUl4WEa9t1Od-N11c6LfPdk0VnGM2NYWfHBbv2bp0EXDFHQoUYNHQt6HR0TDg3u9jH28SxUI2jNMVHFk7aHe3kNqXUrC26-fsnnK6L1tWJoZ36A_dGkKFm9og_3bTvpxllst_eELyRNM="

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