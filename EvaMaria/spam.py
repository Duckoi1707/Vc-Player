import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR

from .darkprince.helpo import modules_help

from config import HNDLR, SUDO_USERS

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command("statspam", prefixes=f"{HNDLR}")
)
async def statspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for _ in range(quantity):
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)
 
@Client.on_message(
    filters.user(SUDO_USERS) & filters.command("spam", prefixes=f"{HNDLR}")
)
async def spam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command("fastspam", prefixes=f"{HNDLR}")
)
async def fastspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.02)
        return

    for _ in range(quantity):
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.02)

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command("slowspam", prefixes=f"{HNDLR}")
)
async def slowspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)


modules_help.append(
    {
        "spam": [
            {"spam [amount of spam]* [spam text]*": "Start spam"},
            {"statspam [amount of spam]* [spam text]*": "Send and delete"},
            {"fastspam [amount of spam]* [spam text]*": "Start fast spam"},
            {"slowspam [amount of spam]* [spam text]*": "Start slow spam"},
        ]
    }
)
