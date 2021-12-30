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
    ('Tuần', 60 * 60 * 24 * 7),
    ('Ngày', 60 * 60 * 24),
    ('Giờ', 60 * 60),
    ('Phút', 60),
    ('Giây', 1)
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
        f"<b>Tốc Độ Của Bot Là🍀</b> `{delta_ping * 100:.3f} ms`"
    )


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
**Sống Ở Xã Hội Này Phải Văn Minh Lịch Sự Một Tí Thì Mới Được Tôn Trọng Chứ Suốt Ngày Ăn Rồi Chửi Tục Đéo Khá Đc Đâu Con Ạ =))**
"""
    await m.reply(GM)


@Client.on_message(filters.command(["gay", "đút đít", "thông đít", "2 đứa con trai", "bê đê"], prefixes=f"{HNDLR}"))
async def goodevening(client, m: Message):
    GE = f"""
<i>Á À Thì Ra Là Mày Bị Gay\n{m.from_user.mention} Thằng Này Bị Gay Nhé Mọi Người</i>
"""
    await m.reply(GE)


@Client.on_message(filters.command(["bot", "", "", "", ""], prefixes=f"{HNDLR}"))
async def goodnight(client, m: Message):
    
    GN = f"""
<i>Nếu Như Mày Có Ý Định Chê Bot Thì Nín Tao Bắt Quả Tang Mày Rồi  </i>
"""
    await m.reply(GN)
  
@Client.on_message(filters.command(["oggy", "", "@oggyvn", "", ""], prefixes=f"{HNDLR}"))
async def ad(client, m: Message):
    AD = f"""
<i> OGGYVN Đẹp Trai Bán VIP Uy tín Ủng Hộ Nó Cho Có Phí Đưa Bạn Gái Đi Nhà Nghỉ </i>
"""
    await m.reply(AD) 
    
    @Client.on_message(filters.command(["Check", "", "", "", ""], prefixes=f"{HNDLR}"))
async def ON(client, m: Message):
    ON = f"""
**Trạng Thái BOT : Hoạt Động ✅ \n<b>⏳ Hoạt Động Được </b> - `{uptime}`**
"""
    await m.reply(ON) 
    
