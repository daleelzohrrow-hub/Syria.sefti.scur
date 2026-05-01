import os
from telethon import TelegramClient, events
from config import api_id, api_hash

client = TelegramClient('session_name', api_id, api_hash)

# قائمة القنوات الشاملة
channels = [
    '@sana_news', '@syriatvnews', '@RudawArabia', '@northpressar', 
    '@HAWAR_NEWS', '@AJASyria', '@almayadeennews', '@sham_fm', 
    '@DamascusNow', '@enabbaladi', '@Step_News', '@syriahr'
]

# كلمات مفتاحية تتعلق بالأمن والسلامة في سوريا
keywords = [
    'انفجار', 'قصف', 'غارة', 'اشتباكات', 'مسيرة', 'طيران', 
    'إغلاق طريق', 'حاجز', 'استهداف', 'عاجل', 'تحذير', 'لغم', 
    'زلزال', 'هزة', 'إطلاق نار', 'هدوء حذر', 'إسعاف', 'حرائق'
]

def update_github():
    print("🔄 تحديث الموقع تلقائياً...")
    os.system("git add .")
    os.system('git commit -m "تحديث أمني عاجل"')
    os.system("git push origin main")

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    news_text = event.raw_text
    
    # فحص إذا كان الخبر يحتوي على إحدى الكلمات المفتاحية
    if any(word in news_text for word in keywords):
        print(f"🚨 خبر أمني مهم: {news_text[:50]}...")
        
        # إضافة الخبر لأعلى الصفحة مع توقيت
        with open('index.html', 'r+', encoding='utf-8') as f:
            content = f.read()
            new_entry = f'<div class="card"><b>⚠️ تحديث أمني:</b><br>{news_text}</div>\n'
            f.seek(0, 0)
            f.write(content.replace('<h1>آخر أخبار السلامة</h1>', f'<h1>آخر أخبار السلامة</h1>\n{new_entry}'))
        
        update_github()
    else:
        print("☁️ خبر عادي (تم تجاهله للحفاظ على نظافة الموقع)")

print("🚀 رادار السلامة يعمل بالفلتر الأمني الآن...")
client.start()
client.run_until_disconnected()

