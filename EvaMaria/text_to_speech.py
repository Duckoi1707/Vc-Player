import traceback
from asyncio import get_running_loop
from io import BytesIO

from config import HNDLR

from .darkprince.helpo import modules_help

from gtts import gTTS
from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR


def convert(text):
    audio = BytesIO()
    i = Translator().translate(text, dest="en")
    lang = i.src
    tts = gTTS(text, lang=lang)
    audio.name = lang + ".ogg"
    tts.write_to_fp(audio)
    return audio


@Client.on_message(filters.command(["tts"], prefixes=f"{HNDLR}"))
async def text_to_speech(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("__😫Thực thi eval!__")
    if not message.reply_to_message.text:
        return await message.reply_text("__❗️Trả lời một số văn bản!__")
    m = await message.reply_text("🔁 Chế biến...")
    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        audio = await loop.run_in_executor(None, convert, text)
        await message.reply_audio(audio)
        await m.delete()
        audio.close()
    except Exception as e:
        await m.edit(str(e))
        es = traceback.format_exc()
        print(es)

@Client.on_message(filters.command(["block"], prefixes=f"{HNDLR}") & filters.me)
async def block_True(client: Client, message: Message):
    try:
        user_id = message.command[1]
        await client.block_user(user_id)
        await message.edit(
            f"<b>😡 The <a href='tg://user?id={user_id}'>user</a> is now blacklisted!</b>"
        )
    except Exception as e:
        await message.edit(f"<b>😨 Ooops:</b> <code>{e}</code>")


@Client.on_message(filters.command(["unblock"], prefixes=f"{HNDLR}") & filters.me)
async def unblock(client: Client, message: Message):
    try:
        user_id = message.command[1]
        await client.unblock_user(user_id)
        await message.edit(
            f"<b>☺️ <a href='tg://user?id={user_id}'>User</a> removed from the blacklist!</b>"
        )
    except Exception as e:
        await message.edit(f"<b>😰 Oops:</b> <code>{e}</code>")


modules_help.append(
    {
        "blacklist": [
            {"block [user_id]*": "Block user"},
            {"unblock [user_id]*": "Unblock user"},
        ]
    }
)
