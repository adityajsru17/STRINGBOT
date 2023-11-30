from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝐇𝐞𝐲 {msg.from_user.mention} 🍷,

𝙸 𝙰𝙼 {me2},

➳ 𝚃𝚁𝚄𝚂𝚃𝙴𝙳 𝚂𝚃𝚁𝙸𝙽𝙶 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁 🫧

➳ 𝙵𝚄𝙻𝙻𝚈 𝚂𝙰𝙵𝙴 𝙰𝙽𝙳 𝚂𝙴𝙲𝚄𝚁𝙴 ⚡️

➳ 𝙽𝙾 𝙴𝚁𝚁𝙾𝚁 💥

𝙼𝙰𝙳𝙴 𝙱𝚈 : 𝗔𝙽𝙾𝙼𝚈𝙽𝙾𝚄𝚂 𝗦𝙰𝚅𝙸𝙾𝚄𝚁𝚂

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🌿 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆 🌿", callback_data="generate")
                ]
            ]
        ),
        
        disable_web_page_preview=True,
    )
