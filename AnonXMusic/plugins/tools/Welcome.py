import os
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from AnonXMusic import LOGGER
from pyrogram.types import Message
from AnonXMusic.misc import SUDOERS
from AnonXMusic import app
from AnonXMusic.CuteDb.Weldb import *
from config import LOGGER_ID

LOGGER = getLogger(__name__)


class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, id, uname):
    background = Image.open("AnonXMusic/assets/WELL2.PNG")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize(
        (420, 420)
    ) 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('AnonXMusic/assets/font.ttf', size=50)
    font2 = ImageFont.truetype('AnonXMusic/assets/font.ttf', size=90)
   # draw.text((65, 250), f'NAME : {unidecode(user)}', fill=(255, 255, 255), font=font)
   # draw.text((65, 340), f'ID : {id}', fill=(255, 255, 255), font=font)
   # draw.text((65, 430), f"USERNAME : {uname}", fill=(255,255,255),font=font)
    pfp_position = (133, 767)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(
        f"downloads/welcome#{id}.png"
    )
    return f"downloads/welcome#{id}.png"


########

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
   # A = await wlcm.find_one({"chat_id" : chat_id})
   # if not A:
  #     return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "assets/NODP.PNG"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption= f"""
ㅤㅤㅤ◦•●◉✿ ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ ✿◉●•◦
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰

● ɴᴀᴍᴇ ➥  {user.mention}
● ᴜsᴇʀɴᴀᴍᴇ ➥  @{user.username}
● ᴜsᴇʀ ɪᴅ ➥  {user.id}

❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ๛𝐆ᴏᴊᴏ ࿐
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰
""",
reply_markup=InlineKeyboardMarkup(
[
[InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Gojoroxbot?startgroup=new"),
]
]
))

    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass

  
