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

# Modifided by Apis
# Cash by rifky

import os
from GroupMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Halo 👋🏻 [{}](tg://user?id={})!**\n\n🤖 Saya adalah bot tingkat lanjut yang dibuat untuk bermain music dalam obrolan suara Grup Telegram & Channel.\n\n✅ Kirimkan saya /help untuk info lebih lanjut."
      HELP_MSG = [
        ".",
f"""
**Hei 👋🏻 Selamat datang kembali di {PROJECT_NAME}

⚪️ {PROJECT_NAME} dapat memutar musik di obrolan suara grup Anda serta obrolan suara saluran (channel)

⚪️ Nama asisten >> @{ASSISTANT_NAME}\n\nKlik berikutnya untuk instruksi lebih lanjut**
""",

f"""
**Pengaturan**

1) Jadikan admin bot (Grup dan di saluran jika menggunakan cplay)
2) Mulai obrolan suara
3) Coba /play [nama lagu] untuk pertama kalinya oleh admin
*) Jika userbot bergabung menikmati music, Jika tidak menambahkan @{ASSISTANT_NAME} ke grup Anda dan coba lagi

**Untuk Channel Music Play**
1) Jadikan saya admin saluran (channel) Anda
2) Kirim /userbotjoinchannel di grup tertaut
3) Sekarang kirim perintah dalam grup tertaut

**Perintah**

**=>> Memainkan Lagu 🎧**

- /play: Putar lagu menggunakan music youtube
- /play [yt url] : Mainkan url yt yang diberikan
- /play [balasan ke audio]: Putar audio yang dijawab
- /dplay: Putar lagu via deezer
- /splay: Putar lagu via jio saavn

**=>> Putar ulang ⏯**

- /player: Buka menu Pengaturan pemutar
- /skip: Lewati trek saat ini
- /pause: Jeda trek
- /resume: Melanjutkan trek yang dijeda
- /end: Menghentikan pemutaran media
- /current: Menunjukkan track yang sedang diputar
- /playlist: Menunjukkan Daftar putar
""",
        
f"""
**=>> Channel Music Play 🛠**

⚪️ Hanya untuk admin grup tertaut:

- /cplay [nama lagu] - putar lagu yang Anda minta
- /cdplay [nama lagu] - putar lagu yang Anda minta melalui deezer
- /csplay [nama lagu] - putar lagu yang Anda minta melalui jio saavn
- /cplaylist - Tampilkan daftar putar sekarang
- /cccurrent - Tampilkan sekarang diputar
- /cplayer - buka panel pengaturan pemutar music
- /cpause - jeda pemutaran lagu
- /cresume - melanjutkan pemutaran lagu
- /cskip - putar lagu berikutnya
- /cend - hentikan pemutaran music
- /userbotjoinchannel - undang asisten ke obrolan Anda

saluran (channel) juga bisa digunakan sebagai pengganti c ( /cplay = /channelplay )

⚪️ Jika Anda tidak suka bermain di grup terkait:

1) Dapatkan ID saluran (channel) Anda.
2) Buat grup dengan judul: Channel Music: your_channel_id
3) Tambahkan bot sebagai admin Saluran dengan perms penuh
4) Tambahkan @{ASSISTANT_NAME} ke saluran sebagai admin.
5) Cukup kirimkan perintah dalam grup Anda.
""",

f"""
**=>> Lebih banyak alat 🧑‍🔧**

- / admincache: Memperbarui info admin grup Anda. Coba jika bot tidak mengenali admin
- / userbotjoin: Undang @{ASSISTANT_NAME} Userbot ke chat Anda

**Pemain cmd dan semua cmds lainnya kecuali** /play, /current  dan /playlist hanya untuk admin grup.
"""
      ]
