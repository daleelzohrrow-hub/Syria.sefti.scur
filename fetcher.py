import feedparser
import os

rss_urls = [
    'https://sana.sy/ar/?feed=rss2',
    'https://www.enabbaladi.net/feed',
    'https://www.syriahr.com/feed/',
    'https://npasyria.com/feed/',
    'https://www.hawarnews.com/ar/feed/',
    'https://www.zamanalwsl.net/rss.php',
    'https://arabic.rt.com/rss/'
]

security_keywords = ['انفجار', 'قصف', 'غارة', 'اشتباك', 'مقتل', 'اعتقال', 'هجوم', 'مسيرة', 'لغم', 'قذيفة', 'ضحايا', 'أمني']

def fetch_and_update():
    found_news = []
    seen_titles = set()

    print("جاري جلب الأخبار...")
    for url in rss_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                title = entry.title
                summary = entry.get('summary', '')
                
                if any(key in title or key in summary for key in security_keywords):
                    if title not in seen_titles:
                        found_news.append({'title': title, 'summary': summary})
                        seen_titles.add(title)
        except:
            continue

    if not found_news:
        print("لم يتم العثور على أخبار جديدة تطابق الكلمات المفتاحية.")
        return

    # قراءة ملف index.html
    if not os.path.exists('index.html'):
        print("خطأ: ملف index.html غير موجود!")
        return

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # تحويل الأخبار إلى صيغة HTML
    html_news = ""
    for news in found_news:
        html_news += f"<div class='card'><h3>📍 {news['title']}</h3><p>{news['summary']}</p></div>\n"

    # إضافة العلامة السرية إذا لم تكن موجودة، ثم استبدالها بالأخبار
    secret_tag = ""
    if secret_tag not in content:
        # وضع العلامة قبل نهاية قسم news-container
        content = content.replace("</div>\n</body>", f"{secret_tag}\n</div>\n</body>")

    new_content = content.replace(secret_tag, html_news + "\n" + secret_tag)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ نجاح! تم إضافة {len(found_news)} خبر جديد للموقع.")

if __name__ == "__main__":
    fetch_and_update()

