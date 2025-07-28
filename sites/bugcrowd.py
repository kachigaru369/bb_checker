import os
import hashlib
from utils.telegram  import send_telegram_message
from playwright.sync_api import sync_playwright

base_url = "https://bugcrowd.com"
list_url = "https://bugcrowd.com/programs"
storage_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'storage', 'company_name'))
os.makedirs(storage_dir,exist_ok=True)

def hash_content(content):
    return hashlib.sha256(content.encode()).hexdigest()

def get_4(page):
    page.goto(list_url,timeout=50000)
    page.wait_for_selector("a.bc-card__container",timeout=50000)
    cards = page.query_selector_all("a.bc-card__container")[:4]
    urls = [base_url+card.get_attribute("href") for card in cards]
    return urls

def check_page(page,url):
    company = url.strip("/").split("/")[-1]
    hash_file = os.path.join(storage_dir,f"{company}.hash")

    page.goto(url, timeout=50000)
    html = page.content()
    new_hash = hash_content(html)

    old_hash = None
    if os.path.exists(hash_file):
        with open(hash_file,'r') as f:
            old_hash = f.read()
    if new_hash != old_hash:
        send_telegram_message(f"new changes! {url}")
        with open(hash_file,'w') as f:
            f.write(new_hash)

    else:
        print(f"no changes: {company}")

def run_background_checker():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            urls = get_4(page)
            for url in urls:
                check_page(page,url)
        finally:
            browser.close()