import datetime
import json
import telethon
import asyncio

async def main():
    api_id = ''
    api_hash = ''

    channel_name = ""

    client = telethon.TelegramClient('session_name', api_id, api_hash)

    await client.start()

    if not client.is_connected():
        await client.connect()

    channel = await client.get_entity(channel_name)

    res = []

    async for message in client.iter_messages(channel):
        if message.media:
            continue
        else:
            print(message.message)
            res.append({"message": message.message})

    with open("messages.json", "w", encoding="utf8") as file:
        json.dump(res, file, ensure_ascii=False)

    await client.log_out()


# comment example

if __name__ == '__main__':
    asyncio.run(main())
