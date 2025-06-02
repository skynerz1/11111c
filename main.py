import time, redis, os, json, re, requests, asyncio
from pyrogram import Client, filters, idle, enums

r = redis.Redis('localhost', decode_responses=True)

# تحميل المعلومات أو طلبها من المستخدم إذا غير موجودة
try:
    from information import *
    Dev_Zaid = token.split(':')[0]
    r.set(f'{Dev_Zaid}botowner', owner_id)
except Exception:
    token = input('[+] Enter the bot token: ')
    Dev_Zaid = token.split(':')[0]
    if not r.get(f'{Dev_Zaid}botowner'):
        owner_id = int(input('[+] Enter SUDO ID: '))
        r.set(f'{Dev_Zaid}botowner', owner_id)
    else:
        owner_id = int(r.get(f'{Dev_Zaid}botowner'))

# جلب اسم البوت
username = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]

to_config = f"""
import redis
r = redis.Redis('localhost', decode_responses=True)
token = '{token}'
Dev_Zaid = '{Dev_Zaid}'
sudo_id = {owner_id}
botUsername = '{username}'

from kvsqlite.sync import Client as DB
ytdb = DB('ytdb.sqlite')
sounddb = DB('sounddb.sqlite')
wsdb = DB('wsdb.sqlite')
"""

with open('config.py', 'w+') as w:
    w.write(to_config)

app = Client(
    f'{Dev_Zaid}r3d',
    14972930,
    'afe0af38c207b1ef65fcfe2c57ef79de',
    bot_token=token,
    plugins={"root": "Plugins"},
)

# ضبط قيم في Redis إذا غير موجودة
if not r.get(f'{Dev_Zaid}:botkey'):
    r.set(f'{Dev_Zaid}:botkey', '⇜')

if not r.get(f'{Dev_Zaid}botname'):
    r.set(f'{Dev_Zaid}botname', 'رعد')

if not r.get(f'{Dev_Zaid}botchannel'):
    r.set(f'{Dev_Zaid}botchannel', 'eFFb0t')

def Find(text):
    pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
    urls = re.findall(pattern, text)
    return [x[0] for x in urls]

app.start()

print('''
[===========================]

█████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░

[===========================]

🔮 Your bot started successfully on R 3 D ☆ Source 🔮

•••••••• @yqyqy66 - @yqyqy66 •••••••••

''')

if r.get(f'DevGroup:{Dev_Zaid}'):
    chat_id = int(r.get(f'DevGroup:{Dev_Zaid}'))
    try:
        app.send_message(chat_id, "تم اتشغيل البوت بنجاح ✔️")
    except Exception as e:
        print("Failed to send start message:", e)

idle()
