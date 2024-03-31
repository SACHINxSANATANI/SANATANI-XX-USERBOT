from Zaid import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "⿕ ʜᴇʏ ɪ ᴀᴍ ᴀ ɪᴅ ᴜsᴇʀ ʙᴏᴛ ⿕\n\n➲ ғᴜʟʟ sᴀғᴇ ʏᴏᴜʀ ᴀᴄᴄ. 101%\n\n⦿ ғɪʀᴀᴛ ɢᴏ ᴛʜɪs ʙᴏᴛ [sᴇssɪᴏɴ-ʙᴏᴛ](https://t.me/SESSION_x_ROBOT)\n⦿ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴠ1\n⦿ ᴛʜᴇɴ ᴄᴏᴍᴇ ʙᴀᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴛʜɪs ʙᴏᴛ\n⦿ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ....\n⦿ /clone (Save Message Code)"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
              [
                  InlineKeyboardButton(text="◎ sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ ◎️", url="https://t.me/SESSION_x_ROBOT"),
              ],
              [
                  InlineKeyboardButton("◎ sᴜᴘᴘᴏʀᴛ ️◎️", url="https://t.me/Il_4ST_FIGHTER_lI"),
                  InlineKeyboardButton("◎ ᴜᴘᴅᴀᴛᴇs ️◎️", url="https://t.me/V_VIP_OWNER"),
              ],
              [
                  InlineKeyboardButton("◎ ᴀʟʟʙᴏᴛ ️◎️", url="https://t.me/Il_4ST_FIGHTER_lI"),
                  InlineKeyboardButton("◎ sᴀᴄʜɪɴ ️◎️", url="https://t.me/V_VIP_OWNER"),
              ],
              ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By Sachin Sanatani Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("💌...𝗣𝗟𝗘𝗔𝗦𝗘 𝗪𝗔𝗜𝗧...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"⿕ 𝗬𝗢𝗨𝗥 𝗜𝗗 𝗨𝗦𝗘𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗔𝗖𝗧𝗜𝗩𝗘 ⿕ {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
