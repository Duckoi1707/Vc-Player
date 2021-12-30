from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR

from .darkprince.helpo import modules_help

digits = {
    str(i): el
    for i, el in enumerate(
        ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    )
}


def prettify(val: int) -> str:
    return "".join(digits[i] for i in str(val))


@Client.on_message(filters.command(["10"], prefixes=f"{HNDLR}"))
async def ghoul_counter(c: Client, m: Message):
    await m.delete()
    counter = 10

    message = await c.send_message(m.chat.id, prettify(counter))

    await sleep(1)

    while counter // 1:
        counter -= 1
        await message.edit_text(prettify(counter))
        await sleep(1)

    await message.edit_text("**Nhìn Ăn Lồn À**")


modules_help.append({"counting": [{"10": "counting from 10 to 0"}]})
