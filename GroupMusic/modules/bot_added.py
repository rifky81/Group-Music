# Ported by Apis

from . import *
from pyrogram import *
from pyrogram.types import *

@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    try:
        btns=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="Channel Support", url="https://t.me/twitter_viralllll")
              ]]
          )

        joiner = await Client.get_me() 
        for user in message.new_chat_members:
            if int(joiner.id) == int(user.id):
                await message.reply_text("👋🏻 Halo kawan , Terima kasih telah menambahkan saya ke Grup Anda\nPromosikan saya sekarang",
    except Exception as e:
        await Client.send_message(int("1711651694"), f"Chat ID: `{message.chat.id}` \nError sambil Mengirim Pesan Terima Kasih: {e}")
