# GroupMusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

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


from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant

from GroupMusic.helpers.decorators import authorized_users_only, errors
from GroupMusic.services.callsmusic.callsmusic import client as USER


@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan saya sebagai admin grup Anda terlebih dahulu</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "RifkyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper sudah berada di obrolan</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n Pengguna {user.first_name} tidak dapat bergabung dengan grup Anda karena berat bergabung dengan permintaan untuk userbot! Pastikan pengguna tidak dibanned dalam grup."
            "\n\nAtau tambahkan secara manual @rifkyyyyyyyyyyyyyyyy ke Grup Anda dan coba lagi</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot bergabung dengan obrolan Anda</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Pengguna tidak dapat keluar dari grup Anda! Mungkin floodwaits."
            "\n\nAtau keluarkan saya secara manual dari ke Grup Anda</b>",
        )
        return

@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Apakah obrolan terhubung?")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan saya sebagai admin saluran (channel) Anda terlebih dahulu</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper sudah berada di saluran (channel)</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n Pengguna {user.first_name} tidak dapat bergabung dengan saluran Anda karena berat bergabung dengan permintaan untuk userbot! Pastikan pengguna tidak dibanned di saluran (channel)."
            "\n\nAtau tambahkan secara manual @rifkyyyyyyyyyyyyyyyy ke Grup Anda dan coba lagi</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot bergabung dengan channel Anda</b>",
    )
    
