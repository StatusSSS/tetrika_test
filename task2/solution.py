import csv
import time
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://ru.wikipedia.org"
START_URL = BASE_URL + "/wiki/Категория:Животные_по_алфавиту"

def parse_page(html, counters):
    soup = BeautifulSoup(html, "html.parser")
    for ul in soup.select("div.mw-category ul"):
        for li in ul.find_all("li"):
            name = li.get_text(strip=True)
            if not name:
                continue
            first = name[0].upper()
            if ("А" <= first <= "Е") or first == "Ё" or ("Ж" <= first <= "Я"):
                counters[first] = counters.get(first, 0) + 1
    nxt = soup.find("a", string="Следующая страница")
    if nxt and nxt.get("href"):
        return BASE_URL + nxt["href"]
    return None


def collect_beasts():
    url = START_URL
    counts = {}
    sess = requests.Session()
    while url:
        r = sess.get(url)
        r.raise_for_status()
        url = parse_page(r.text, counts)
        time.sleep(0.3)
    letters = [chr(c) for c in range(ord('А'), ord('Е')+1)] + ['Ё'] + [chr(c) for c in range(ord('Ж'), ord('Я')+1)]
    for l in letters:
        counts.setdefault(l, 0)
    return counts


def save_csv(data, filename="beasts.csv"):
    letters = [chr(c) for c in range(ord('А'), ord('Е')+1)] + ['Ё'] + [chr(c) for c in range(ord('Ж'), ord('Я')+1)]
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for l in letters:
            writer.writerow([l, data[l]])


if __name__ == "__main__":
    stats = collect_beasts()
    save_csv(stats)
    print("beasts.csv создан, всего букв:", len(stats))
