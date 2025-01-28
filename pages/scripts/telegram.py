from telethon.sync import TelegramClient
from os import environ
import asyncio


class TeleGram:
    def __new__(self, msg: str) -> None:
        api_id = environ.get("API_ID")
        api_hash = environ.get("API_HASH")
        contact = environ.get("CONTACT_TELEGRAM")
        bot_token = environ.get("BOT_TOKEN")

        async def send_message() -> None:
            client = TelegramClient("bot", api_id, api_hash)
            await client.start(bot_token=bot_token)
            async with client:
                await client.send_message(contact, msg)

        asyncio.run(send_message())
        return None
