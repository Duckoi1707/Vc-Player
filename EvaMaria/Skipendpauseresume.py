from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from EvaMaria.helpers.decorators import authorized_users_only
from EvaMaria.helpers.handlers import skip_current_song, skip_item
from EvaMaria.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["skip"], prefixes=f"{HNDLR}"))
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**🙄Không có gì trong hàng đợi để bỏ qua!**")
        elif op == 1:
            await m.reply("**😩Empty Queue, Rời khỏi cuộc trò chuyện thoại**")
        else:
            await m.reply(
                f"**⏭ Đã bỏ qua** \n**🎧 Đang chơi** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ Đã xóa các bài hát sau khỏi Hàng đợi: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.command(["end", "stop"], prefixes=f"{HNDLR}"))
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**😐Chấm dứt**")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**🤨Không có gì đang chơi !**")


@Client.on_message(filters.command(["pause"], prefixes=f"{HNDLR}"))
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸Đã tạm dừng.**\n\n• Để tiếp tục phát lại, hãy sử dụng lệnh » {HNDLR}resume"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**🤨Không có gì đang chơi!**")


@Client.on_message(filters.command(["resume"], prefixes=f"{HNDLR}"))
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ Tiếp tục**\n\n• Để tạm dừng phát lại, hãy sử dụng lệnh » {HNDLR}pause**"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**🙄 Hiện không có gì bị tạm dừng!**")
