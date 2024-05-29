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
    "•──────────────────────•\n❍ 𝗛𝗘𝗬 ‣ 𝗠𝗬 𝗗𝗘𝗔𝗥 𝗨𝗦𝗘𝗥\n•──────────────────────•\n❍ 𝗜 𝗔𝗠 ‣ ‌ ‌𝗨𝗦𝝣𝗥𝗕𝚯𝗧 || 𝗕𝚯𝗧\n•──────────────────────•\n⦿ ғɪʀᴀᴛ ɢᴏ ᴛʜɪs ʙᴏᴛ [sᴇssɪᴏɴ-ʙᴏᴛ](https://t.me/SESSIONxGENxBOT)\n⦿ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴠ1\n⦿ ᴛʜᴇɴ ᴄᴏᴍᴇ ʙᴀᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴛʜɪs ʙᴏᴛ\n⦿ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴜsʀʙᴏᴛ....\n⦿ /clone (Save Message Code)\n•──────────────────────•\n           [❖ │ sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ │ ❖](https://t.me/all_sanatani_bot)\n•──────────────────────•"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
              [
                  InlineKeyboardButton(text="🍁 sᴇssɪᴏɴ ɢᴇɴ ʙᴏᴛ 🍁️", url="https://t.me/SESSIONxGENxBOT"),
              ],
              [
                  InlineKeyboardButton("💫 sᴀᴄʜɪɴ️", url="https://t.me/SACHIN_OWNER"),
                  InlineKeyboardButton("ʀᴇᴘᴏ ✨️", url="https://t.me/+cW07X2RM_IBmYTI1"),
              ],
              [
                  InlineKeyboardButton("🌹 sᴜᴘᴘᴏʀᴛ️", url="https://t.me/+cW07X2RM_IBmYTI1"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs 🌸️", url="https://t.me/ALL_SANATANI_BOT"),
              ],
              ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By Sachin Sanatani Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("❍ HOW TO USE \n\n𔓕 /clone session \n𔓕 /clone save msg code")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("❖ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"❖ ɴᴏᴡ ʏᴏᴜ ᴀʀᴇ ʀᴇᴀᴅʏ ᴛᴏ ғɪɢʜᴛ\n\n❍ [❖ │ sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ │ ❖](https://t.me/all_sanatani_bot)\n\n❖ {user.first_name}")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
