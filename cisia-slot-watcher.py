import time
import requests
from bs4 import BeautifulSoup


URL = "https://testcisia.it/calendario.php?tolc=cents&l=gb&lingua=inglese" 
CHECK_EVERY_SECONDS = 60
KEYWORDS = ["AVAILABLE"]  

BOT_TOKEN = "*"
CHAT_ID = "*"

HEADERS = {"User-Agent": "Mozilla/5.0 (CISIA-Availability-Checker)"}

def send_telegram(text: str) -> None:
    api = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(api, json={"chat_id": CHAT_ID, "text": text}, timeout=15)
    if r.status_code != 200:
        print("Telegram error:", r.status_code, r.text)
    r.raise_for_status()

def fetch_html(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.text

def find_home_available_rows(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    hits = []

    for tr in soup.select("table tr"):
        row_text = tr.get_text(" ", strip=True)
        if not row_text:
            continue

        t = row_text.upper()
        if "AVAILABLE" in t and "@HOME" in t:
            hits.append(row_text)

    return hits

def main():
    send_telegram("CISIA watcher started. I will alert you ONLY if CEnT-S@HOME shows AVAILABLE.")

    last_fp = None

    while True:
        try:
            html = fetch_html(URL)
            hits = find_home_available_rows(html)

            fp = "|".join(hits) if hits else ""

            
            if hits and fp != last_fp:
                msg = "SLOT FOUND (CEnT-S@HOME)\n\n" + "\n---\n".join(hits[:3])
                send_telegram(msg)
                last_fp = fp

        except Exception as e:
            try:
                send_telegram(f"Watcher error: {e}")
            except:
                pass
            time.sleep(120)

        time.sleep(CHECK_EVERY_SECONDS)

if __name__ == "__main__":
    main()