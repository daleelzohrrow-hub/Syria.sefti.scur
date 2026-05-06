import feedparser
from datetime import datetime

# 1. قائمة المصادر الشاملة
rss_urls = [
    'https://sana.sy/ar/?feed=rss2',
    'https://www.enabbaladi.net/feed',
    'https://www.syriahr.com/feed/',
    'https://npasyria.com/feed/',
    'https://www.hawarnews.com/ar/feed/',
    'https://www.zamanalwsl.net/rss.php'
]

security_keywords = ['انفجار', 'قصف', 'غارة', 'اشتباك', 'عبوة', 'أمني', 'سلامة', 'طريق', 'مغلق', 'اعتقال']

def run():
    # الحصول على الوقت الحالي بتوقيت سوريا (تقريباً)
    now = datetime.now().strftime('%Y-%m-%d %I:%M %p')
    found_news = []
    
    for url in rss_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                if any(key in entry.title for key in security_keywords):
                    # إضافة الخبر مع توقيت رصده
                    found_news.append(f"""
                    <div style='border-bottom:1px solid #ccc; padding:10px;'>
                        <h3 style='color:red;'>⚠️ {entry.title}</h3>
                        <p>{entry.summary}</p>
                        <small>تم الرصد في: {now}</small>
                    </div>""")
        except:
            continue

    if found_news:
        with open('index.html', 'a', encoding='utf-8') as f:
            f.write("\n".join(found_news))
        print(f"تمت إضافة {len(found_news)} أخبار جديدة في تمام الساعة {now}")
    else:
        print(f"فحص دوري في {now}: لا توجد أخبار أمنية جديدة.")

run()

