import os


try:
     import signal
except:
     os.system("pip install signal")
     import signal
# noinspection PyPackageRequirements
try:
     import ffmpeg
except:
     os.system("pip install ffmpeg-python")
     import ffmpeg
from pyrogram import Client, filters
from pyrogram.types import Message
from DaisyXMusic.modules.song import get_text
from DaisyXMusic.services.callsmusic import callsmusic  # pip install pytgcalls
from DaisyXMusic.helpers.decorators import authorized_users_only

# Example of pinned message in a chat:
'''
Radio stations:
1. https://hls-01-regions.emgsound.ru/11_msk/playlist.m3u8
To start replay to this message with command !start <ID>
To stop use !stop command
'''



GROUP_CALLS = {}
FFMPEG_PROCESSES = {}


@Client.on_message(filters.command('broadcast'))
@authorized_users_only
async def start(client, message: Message):
    await message.reply("Processing")
    input_filename = f'radio-{message.chat.id}.raw'
    chat_id = message.chat.id
    if message.chat.id in callsmusic.pytgcalls.active_calls:
         await message.reply("Try again after ending music play")
         return         

    process = FFMPEG_PROCESSES.get(message.chat.id)
    if process:
        process.send_signal(signal.SIGTERM)

    station_stream_url = None
    query = get_text(message)
    station_id = query
    msg_lines = message.reply_to_message.text.split('\n')
    for line in msg_lines:
        line_prefix = f'{station_id}. '
        if line.startswith(line_prefix):
            station_stream_url = (
                line.replace(line_prefix, '').replace('\n', '')
            )
            break

    if not station_stream_url:
        await message.reply_text(f'Can\'t find a station with id {station_id}')
        return

    try:
        callsmusic.pytgcalls.join_group_call(chat_id, input_filename)
    except:
        res.edit("Group call is not connected of I can't join it")
        return

    process = ffmpeg.input(station_stream_url).output(
        input_filename,
        format='s16le',
        acodec='pcm_s16le',
        ac=2,
        ar='48k'
    ).overwrite_output().run_async()
    FFMPEG_PROCESSES[message.chat.id] = process

    await message.reply_text(f'Radio #{station_id} is playing...')


@Client.on_message(filters.command('stopbrodcast'))
@authorized_users_only
async def stop(_, message: Message):
    callsmusic.pytgcalls.leave_group_call(message.chat.id)
    process = FFMPEG_PROCESSES.get(message.chat.id)
    if process:
        process.send_signal(signal.SIGTERM)
    await message.reply("Stopped radio/music streaming")
