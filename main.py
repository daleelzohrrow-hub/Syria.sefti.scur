from telethon import TelegramClient, events
import config

client = TelegramClient('session_name', 2040, 'b18441a1ff607e10a989891a5462e627')

@client.on(events.NewMessage(chats=['@Sana_English', '@syriatvnews']))
async def handler(event):
    print(f"خبر جديد: {event.raw_text}")
    with open("news.txt", "a", encoding="utf-8") as f:
        f.write(event.raw_text + "\n---\n")

print("البوت يعمل الآن... بانتظار الأخبار")
client.start()
client.run_until_disconnected()
API_ID = 2040
API_HASH = 'b18441a1ff607e10a989891a5462e627'
# ضع هنا معرفات القنوات التي تريد مراقبتها (مثال)
CHANNELS = ['@Sana_English', '@syriatvnews'] 

