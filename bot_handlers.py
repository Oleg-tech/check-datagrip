from bot import bot
from db import *

CONTENT_TYPES = ["text",
                 "sticker",
                 "document",
                 "photo",
                 "audio",
                 "video",
                 "video_note",
                 "voice",
                 "location",
                 "contact"
                 ]
GROUP_ID = -1001691283602


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"hi!!!\n{message.from_user.username}")
    regestration(message.from_user.id, message.from_user.username)
    update_messages_count(message.from_user.id)


@bot.message_handler(commands=["stats"])
def get_stats(message):
    bot.reply_to(message,
                 get_stats_messsage(),
                 disable_web_page_preview=True,
                 parse_mode="HTML")
    update_messages_count(message.from_user.id)


@bot.message_handler(content_types=CONTENT_TYPES, func=lambda message: message.chat.id == GROUP_ID, )
def message_from_user(message):
    update_messages_count(message.from_user.id)