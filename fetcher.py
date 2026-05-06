import feedparser

# 1. قائمة مصادر شاملة لكل الجغرافيا السورية
rss_urls = [
    'https://sana.sy/ar/?feed=rss2',          # الوكالة الرسمية (دمشق)
    'https://www.enabbaladi.net/feed',         # عنب بلدي (مستقلة)
    'https://www.syriahr.com/feed/',           # المرصد السوري لحقوق الإنسان
    'https://npasyria.com/feed/',              # نورث برس (North Press)
    'https://www.hawarnews.com/ar/feed/',      # وكالة هاوار (ANHA)
    'https://www.zamanalwsl.net/rss.php',      # زمان الوصل
    'https://arabic.rt.com/rss/',              # تغطية دولية/محلية
]

# 2. كلمات مفتاحية أمنية دقيقة
security_keywords = [
    'انفجار', 'قصف', 'غارة', 'اشتباك', 'عبوة', 'مداهمة', 'اعتقال',
    'اغتيال', 'حاجز', 'طريق', 'لغم', 'مسيرة', 'استهداف', 'أمني'
]

def fetch_and_update():
    found_news = []
    seen_titles = set()

    for url in rss_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                title = entry.title
                summary = entry.get('summary', '')
                
                # التحقق من الكلمات المفتاحية وعدم التكرار
                if any(key in title or key in summary for key in security_keywords):
                    if title not in seen_titles:
                        found_news.append({'title': title, 'summary': summary})
                        seen_titles.add(title)
        except:
            continue
            
    if found_news:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        news_html = ""
        for news in found_news[:10]:
            news_html += f"<div class='card'><h3>⚠️ {news['title']}</h3><p>{news['summary']}</p></div>\n"

        # إضافة الأخبار الجديدة في المكان المخصص
        updated_content = content.replace("<div class='news-container'>", f"<div class='news-container'>\n{news_html}")
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"تم إضافة {len(found_news)} خبر من مصادر متنوعة.")

fetch_and_update()

