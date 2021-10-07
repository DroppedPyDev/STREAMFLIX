

import os
from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class CatX_botz(object):
        admins = {}
        BOT_TOKEN = getenv("BOT_TOKEN", None)
        CHANNEL = int(os.getenv('CHANNEL', 123456))
        API_ID = int(getenv("API_ID", "6"))
        API_HASH = getenv("API_HASH", "")
        SESSION_NAME = getenv("SESSION_NAME", None)
        DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
        SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
        ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
        BOT_USERNAME = getenv("BOT_USERNAME", "")
        COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
        CHANNEL_NAME = getenv("CHANNEL_NAME", "CatX_botz")
        GROUP_NAME = getenv("GROUP_NAME", "CatX_botz_chat")
        OWNER_NAME = getenv("OWNER_NAME", "Telecat_X")


# Edits these lines with your own values⚙️
