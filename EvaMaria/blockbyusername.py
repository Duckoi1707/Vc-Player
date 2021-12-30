from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR

from .darkprince.helpo import modules_help


@Client.on_message(filters.command(["block"], prefixes=f"{HNDLR}"))
async def block_True(client: Client, message: Message):
    try:
        user_id = message.command[1]
        await client.block_user(user_id)
        await message.reply_text(
            f"<b>😡 The <a href='tg://user?id={user_id}'>user</a> bây giờ đã được đưa vào danh sách đen!</b>"
        )
    except Exception as e:
        await message.reply_text(f"Lỗi")


@Client.on_message(filters.command(["unblock"], prefixes=f"{HNDLR}"))
async def unblock(client: Client, message: Message):
    try:
        user_id = message.command[1]
        await client.unblock_user(user_id)
        await message.reply_text(
            f"<b>☺️ <a href='tg://user?id={user_id}'>User</a> removed from the blacklist!</b>"
        )
    except Exception as e:
        await message.reply_text(f"Lỗi Vui Lòng Thử Lại")


modules_help.append(
    {
        "blacklist": [
            {"block [user_id]*": "Block user"},
            {"unblock [user_id]*": "Unblock user"},
        ]
    }
)
