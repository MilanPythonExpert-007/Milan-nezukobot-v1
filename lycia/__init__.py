import os
from pyrogram import Client

API_ID = os.environ.get("24082016", None)
API_HASH = os.environ.get("81af1b2969f06110e0901aa41bfb932d", None)
TOKEN = os.environ.get("8084842403:AAEUFB_06TBlAhy3J-0daAMQwL7nqHBsLsk", None)

LYCIA = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
