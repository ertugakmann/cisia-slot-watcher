# CISIA CEnT-S Slot Watcher

A small Python tool that monitors the official CISIA CEnT-S calendar page and sends instant Telegram notifications when a **CEnT-S@HOME** slot becomes **AVAILABLE**.

## 🚩 Problem

CEnT-S test slots are highly competitive and often disappear within minutes. Manually refreshing the page all day is not practical and makes it easy to miss newly opened slots.

## 💡 Solution

I built a lightweight Python monitoring script that:

- Periodically checks the official CISIA calendar page
- Parses the HTML using BeautifulSoup
- Looks specifically for **table rows** containing both `CEnT-S@HOME` and `AVAILABLE`
- Sends an instant Telegram notification when a matching slot appears

This way, I can react immediately when a new slot is published.

## ✨ Features

- Checks the page at a configurable interval
- Filters only **CEnT-S@HOME** availability (no false alarms from legends or headers)
- Sends real-time alerts via Telegram
- Simple and lightweight (uses `requests` + `beautifulsoup4`)

## 🛠️ Tech Stack

- Python 3  
- requests  
- beautifulsoup4  
- Telegram Bot API  

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/ertugakmann/cisia-slot-watcher.git
cd cisia-slot-watcher
