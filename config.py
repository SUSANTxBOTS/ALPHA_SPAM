import logging

from telethon import TelegramClient

from os import getenv
from RAUSHAN.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = "21134445"
API_HASH = "231c18ea7273824491d6bf05425ab74e"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

BOT_TOKEN = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN2 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN3 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN4 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN5 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN6 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN7 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN8 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN9 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")
BOT_TOKEN10 = getenv("8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="8156708830").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8156708830"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X2 = TelegramClient('X2', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X3 = TelegramClient('X3', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X4 = TelegramClient('X4', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X5 = TelegramClient('X5', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X6 = TelegramClient('X6', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X7 = TelegramClient('X7', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X8 = TelegramClient('X8', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X9 = TelegramClient('X9', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')
X10 = TelegramClient('X10', 21134445, '231c18ea7273824491d6bf05425ab74e').start(bot_token='8295104109:AAH0o8V1ebA7uA136yrhoCBYy7kLmhIPjFk')





