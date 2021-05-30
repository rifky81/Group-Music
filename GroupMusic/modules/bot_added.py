
# GroupMusic (Telegram bot project )
# Copyright (C) 2021  Apis

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
