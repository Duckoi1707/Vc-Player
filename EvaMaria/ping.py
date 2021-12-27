import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>Tôi đang trực tuyến🍀</b> `{delta_ping * 100:.3f} ms` \n<b>⏳Uptime </b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**🖥️System🖱️Restarted⌨️**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<i>🤓Xin Chào {m.from_user.mention}!

🛠 HỖ TRỢ MENU
⚡ LỆNH CƠ BẢN
❍ {HNDLR}help - để xem danh sách các lệnh
❍ {HNDLR}play [tên bài hát | liên kết youtube | trả lời tệp âm thanh] - để phát một bài hát
❍ {HNDLR}vplay [tiêu đề video | liên kết youtube | trả lời tệp video] - để phát video
❍ {HNDLR}playlist để xem danh sách phát
❍ {HNDLR}ping - để kiểm tra trạng thái
❍ {HNDLR}resume - để tiếp tục phát một bài hát hoặc video
❍ {HNDLR}pause - để tạm dừng phát lại một bài hát hoặc video
❍ {HNDLR}skip - để bỏ qua các bài hát hoặc video
❍ {HNDLR}end - để kết thúc phát lại</i>
"""
    await m.reply(HELP)

@Client.on_message(filters.command(["đm", "lồn", "cặc", "địt mẹ"], prefixes=f"{HNDLR}"))
async def goodmorning(client, m: Message):
    GM = f"""
<i>Mẹ Mày Mồm Hư Lắm Nhá Ban Cm Mày Giờ </i>
"""
    await m.reply(GM)


@Client.on_message(filters.command(["Good Evening", "Gud evng", "gud evening", "ഗുഡ് ഈവനിംഗ്", "ഗുഡ് ഈവെനിംഗ്"], prefixes=f"{HNDLR}"))
async def goodevening(client, m: Message):
    GE = f"""
<i> 😁Gøød Evening..☕️</i>
"""
    await m.reply(GE)


@Client.on_message(filters.command(["bot", "Gud nt", "gud night", "ഗുഡ് നൈറ്റ്‌", "gudnyt"], prefixes=f"{HNDLR}"))
async def goodnight(client, m: Message):
    
    GN = f"""
<i>Nhắc Cái Gì Tính Chê Hay Gì Địt Mẹ </i>
"""
    await m.reply(GN)
  
@Client.on_message(filters.command(["oggy", "OGGY", "@oggyvn", "ഗുഡ് നൈറ്റ്‌", "gudnyt"], prefixes=f"{HNDLR}"))
async def ad(client, m: Message):
    AD = f"""
<i>OGGY ĐẸP TRAI VÍP BỜ RỒ </i>
"""
    await m.reply(AD) 
    
@Client.on_message(filters.command(["test", "", "", "", ""], prefixes=f"{HNDLR}"))
async def test(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("10")
    await loli.edit("11")
    await loli.edit("12")
    await loli.edit("13")
    await loli.edit("14")
    await loli.edit("15")
    await loli.edit("16")
    await loli.edit("17")
    await loli.edit("**Địt Mẹ Chúng Mày**")
