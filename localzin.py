from playwright.sync_api import sync_playwright
import re

def run_scraper(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        all_links = page.locator('a')
        all_h3_texts = page.locator('h3').all_inner_texts()
        r = re.compile(r".*(dados|python)", re.IGNORECASE)
        filtered_h3_texts = list(filter(r.match, all_h3_texts)) 
        print(all_links)
        browser.close()
        return filtered_h3_texts


result = run_scraper('https://www.sympla.com.br/produtor/digitalcollegebr')
print(f"{result}")
