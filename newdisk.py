from pyrogram import Client as ub
from pyrogram import filters
from pyrogram.client import Client
from pyrogram.raw import types, functions
from pyrogram.methods.messages import Messages
from apscheduler.schedulers.background import BackgroundScheduler
from gtt import get_thump
from gencover import gen_cover
import time
import os
from os import getenv

ss = getenv("SESSION")
a1 = int(getenv("API_ID"))
a2 = getenv("API_HASH")


kutty = Client(ss, 
        api_id=a1, 
        api_hash=a2)


def starting():
    for vid in kutty.search_messages(-1001707716901, filter='video', limit=1):
        bv = kutty.copy_message('@mdisk7bot', from_chat_id= -1001707716901, message_id=vid.message_id)
        vid.download(file_name=f'res/{bv.message_id}.mp4')
        vid.delete()
        get_thump(f'res/{bv.message_id}.mp4', f'{bv.message_id}.png')
        gen_cover(f'{bv.message_id}.png', bv.message_id)
        time.sleep(1)
        if vid.caption == None:
            g = kutty.send_message('@mdisk7bot', text=f'new hot video')
        else:
            g = kutty.send_message('@mdisk7bot', text=vid.caption)
        print(g.message_id)
    else:   
        print('Ok............')
    


@kutty.on_message(filters.command('id', '.') & filters.me)
def get_id(__, m:Messages):
    m.edit(f'chat id is  `{m.chat.id}`')   

@kutty.on_message(filters.regex(r'https://mdisk.me/') & filters.user('@mdisk7bot'))
def get_link(__, m:Messages):
    print(m)
    time.sleep(1)
    file_caption = m.reply_to_message.caption
    if file_caption == None:
        file_caption = 'Top video Today 😍'
    c1 = kutty.send_photo('@AD_Mdisk_Bot', photo=f'final{m.reply_to_message.message_id}.png',
                    caption=f'**TAG : {file_caption}**'
                            f'\n**{m.text}**')
    # c1.copy(-1001626342573)
    # b1 = c1.copy('pdisk_link_adminbot')
    # kutty.send_message('pdisk_link_adminbot', text='/broadcast', reply_to_message_id=b1.message_id)
    time.sleep(1)
    os.remove(f'final{m.reply_to_message.message_id}.png')
    os.remove(f'{m.reply_to_message.message_id}.png')
    os.remove(f'res/{m.reply_to_message.message_id}.mp4')

scheduler = BackgroundScheduler()
scheduler.add_job(starting, 'interval' , seconds=60)


scheduler.start()




kutty.run()
