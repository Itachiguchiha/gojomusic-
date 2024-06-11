import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from AnonXMusic import app  

ABHI = [
"https://telegra.ph/file/29d7979fe9482ffc58498.jpg",
"https://telegra.ph/file/ceb800f02380a8528199f.jpg",
"https://telegra.ph/file/45f59b0999739161dfbdc.jpg"
"https://telegra.ph/file/c03ad16296f3c40926e09.jpg",
"https://telegra.ph/file/1e1e109b842faa2047e05.jpg",
"https://telegra.ph/file/caa64fac5dcb9d03b93c8.jpg",
"https://telegra.ph/file/c52ab40540022d4239f53.jpg",
"https://telegra.ph/file/b4e212e5969b0638ca801.jpg",
"https://telegra.ph/file/0447de9d4ab3bef79c5e5.jpg",
"https://telegra.ph/file/1f428c35a4346b11903dc.jpg",
"https://telegra.ph/file/a2e1d1c09567d143c5f0c.jpg",
"https://telegra.ph/file/19deb18bedf10a4c11665.jpg",
"https://telegra.ph/file/7da22eb5cd6cfb35df303.jpg",
"https://telegra.ph/file/a94ff1c09937542e40794.jpg",

]

NYKAA = [
"https://telegra.ph/file/fd1a5657f31f815492f37.jpg",
"https://telegra.ph/file/4d1b9889c4dd3316c945d.jpg",
"https://telegra.ph/file/1d6eecfde30b0afcd8edb.jpg",
"https://telegra.ph/file/61e60b8fede23ba51be92.jpg",
"https://telegra.ph/file/e6dff3fceb9eaac8d3ee8.jpg",
"https://telegra.ph/file/537cb7f3e8aa02597c99e.jpg",
"https://telegra.ph/file/537cb7f3e8aa02597c99e.jpg",
"https://telegra.ph/file/1c9ab57a404bb1be0f799.jpg",
"https://telegra.ph/file/aaeb5edb3b92e2079e580.jpg",
"https://telegra.ph/file/97ea498a4d1254cd56bb8.jpg",
"https://telegra.ph/file/4d78d59aac5d87ffe5f36.jpg",
"https://telegra.ph/file/97c9f004ab66ebc788992.jpg",
"https://telegra.ph/file/3ecba5e36cff7580fc8a9.jpg",
"https://telegra.ph/file/98a6ae06256990bef97f1.jpg",
"https://telegra.ph/file/0ed8a1dd3b5fe8351eee0.jpg",
"https://telegra.ph/file/6ddb70ce10a1c04291cd9.jpg",
"https://telegra.ph/file/9372dd161b24366e9c785.jpg",
"https://telegra.ph/file/978a926f3a03ec9f44458.jpg",
"https://telegra.ph/file/a6f291585b6984e947d6d.jpg",
"https://telegra.ph/file/b7707550eea03f2c3ea68.jpg",
"https://telegra.ph/file/f01d23ce8652da3a5468d.jpg",
"https://telegra.ph/file/6fa25d447abfdac785559.jpg",
"https://telegra.ph/file/c5ea043ac5609753986fc.jpg",
"https://telegra.ph/file/e82638529bd936e075181.jpg",
"https://telegra.ph/file/3d5d351a6b7cf73940353.jpg",
"https://telegra.ph/file/09e3b2247ec91e858103c.jpg",
"https://telegra.ph/file/7a9abce2a8a5850c61781.jpg",
"https://telegra.ph/file/503b4ded6e89b9ecac81b.jpg",
"https://telegra.ph/file/9c1f96cb74b200d6c50e7.jpg",
]



@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❖ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❖\n\n"
               
                f"● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {message.chat.title}\n"
                f"● ɢʀᴏᴜᴘ ɪᴅ ➥ {message.chat.id}\n"
                f"● ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➥ @{message.chat.username}\n"
                f"● ɢʀᴏᴜᴘ ʟɪɴᴋ ➥ [ʙᴀʙʏ ᴛᴏᴜᴄʜ]({link})\n"
                f"● ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➥ {count}\n\n"
                f"❖ ᴀᴅᴅᴇᴅ ʙʏ ➥ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(ABHI), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"❖ <b>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</b> ❖\n\n● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {title}\n\n● ɢʀᴏᴜᴘ ɪᴅ ➥ {chat_id}\n\n● ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➥ {remove_by}\n\n❖ ʙᴏᴛ ɴᴀᴍᴇ ➥ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(NYKAA), caption=left, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❖ ʜᴇʏ {message.from_user.mention} ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ ❖\n\n"
                
                f"● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {message.chat.title}\n"
                f"● ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➥ @{message.chat.username}\n\n"
                f"● ʏᴏᴜʀ ɪᴅ ➥ {member.id}\n"
                f"● ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ ➥ @{member.username}\n\n"
                f"❖ ʏᴏᴜ ᴀʀᴇ {count}ᵀᴴ ᴍᴇᴍʙᴇʀ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ."
            )
            await app.send_photo(message.chat.id, photo=random.choice(NYKAA), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))



      
