import requests
from bs4 import BeautifulSoup
from collections import Counter
import re


def analyze_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося отримати сторінку: {e}")
        return

    soup = BeautifulSoup(html_content, 'html.parser')

    text = soup.get_text()
    words = re.findall(r'\b\w+\b',
                       text.lower())
    word_counts = Counter(words)

    print("Частота появи слів у тексті новини:")
    for word, count in word_counts.most_common(
            10):
        print(f"{word}: {count}")

    tags = [tag.name for tag in soup.find_all()]
    tag_counts = Counter(tags)

    print("\nЧастота появи HTML-тегів:")
    for tag, count in tag_counts.most_common(
            10):
        print(f"<{tag}>: {count}")

    links = soup.find_all('a')
    print(f"\nКількість посилань на сторінці: {len(links)}")

    images = soup.find_all('img')
    print(f"Кількість зображень на сторінці: {len(images)}")


url = input("Введіть URL сторінки новин для аналізу: ")
analyze_webpage(url)