import os
import asyncio
from telethon import TelegramClient, events

# --- 1. ضع بياناتك هنا ---
api_id = 2040          # امسح الرقم وضع رقمك (بدون علامات تنصيص)
api_hash = 'b18441a1ff607e10a989891a5462e627'    # امسح الكلمة وضع الهاش الخاص بك (داخل علامات التنصيص)
# -------------------------

client = TelegramClient('safety_session', api_id, api_hash)

# 2. قائمة القنوات (الشاملة لكل المناطق السورية)
channels = [
    '@sana_news', '@syriatvnews', '@RudawArabia', '@northpressar', 
    '@HAWAR_NEWS', '@AJASyria', '@almayadeennews', '@sham_fm', 
    '@DamascusNow', '@enabbaladi', '@Step_News', '@syriahr'
]

# 3. الكلمات المفتاحية المتعلقة بالأمن والسلامة
keywords = [
    'انفجار', 'قصف', 'غارة', 'اشتباكات', 'مسيرة', 'طيران', 
    'إغلاق طريق', 'حاجز', 'استهداف', 'عاجل', 'تحذير', 'لغم', 
    'زلزال', 'هزة', 'إطلاق نار', 'هدوء حذر', 'إسعاف', 'حرائق'
]

def update_github():
    """وظيفة رفع التحديثات إلى GitHub تلقائياً"""
    print("🔄 جاري مزامنة الأخبار مع الموقع...")
    os.system("git add .")
    os.system('git commit -m "تحديث أمني تلقائي"')
    os.system("git push origin main")
    print("✅ تم تحديث الموقع بنجاح!")

@client.on(events.NewMessage())
async def my_event_handler(event):
    news_text = event.raw_text
    
    # فحص الكلمات المفتاحية
    if any(word in news_text for word in keywords):
        print(f"🚨 التقطت خبراً مهماً: {news_text[:50]}...")
        
        # إضافة الخبر بتنسيق HTML جميل في أعلى الصفحة
        with open('index.html', 'r+', encoding='utf-8') as f:
            content = f.read()
            # التنسيق الجديد للخبر داخل كرت (Card)
            new_entry = f'''
            <div style="border-right: 5px solid #e74c3c; background: #fff5f5; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                <strong style="color: #e74c3c;">⚠️ تنبيه أمني عاجل:</strong><br>
                <p>{news_text}</p>
                <small style="color: #7f8c8d;">المصدر: تقرير أمني</small>

            </div>
            '''
            # وضع الخبر مباشرة تحت عنوان الصفحة الرئيسي
            f.seek(0, 0)
            f.write(content.replace('', f'\n{new_entry}'))
        
        update_github()
    else:
        print("☁️ خبر عادي، تم تخطيه.")

print("🚀 رادار السلامة السوري بدأ العمل... بانتظار الأخبار العاجلة")
client.start()
client.run_until_disconnected()

