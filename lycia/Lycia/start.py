from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
I am Nezuko-Chan, An Intelligent ChatBot
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Group manager Bot", url = "https://t.me/yumekojabami_robot"), InlineKeyboardButton("Github", url = "https://github.com/DEVILTG/Nezukochanchatbot"), InlineKeyboardButton("Support Group", url = "https://t.me/devils_territory")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
