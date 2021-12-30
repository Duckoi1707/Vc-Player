from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR

from .darkprince.helpo import modules_help


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["block"], prefixes=f"{HNDLR}")
)
async def block_True(client: Client, message: Message):
    try:
        user_id = message.command[1]
        await client.block_user(user_id)
        await message.edit(
            f"Bạn Đã Bị Đưa Vào Danh Sách Đen"
        )
    except Exception as e:
        await message.edit(f"Lỗi : Bạn Phải Tag Username Hoặc ID Người Dùng") 


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["unblock"], prefixes=f"{HNDLR}")
)
async def unblock(client: Client, message: Message):
    try:
        user_id = message.command[1]
        await client.unblock_user(user_id)
        await message.edit(
            f"Bạn Đã Được Mở Lại"
        )
    except Exception as e:
        await message.edit(f"Bạn Không Đủ Quyền Hạn")


modules_help.append(
    {
        "blacklist": [
            {"block [user_id]*": "Block user"},
            {"unblock [user_id]*": "Unblock user"},
        ]
    }
)
