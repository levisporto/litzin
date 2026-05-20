from playwright.sync_api import sync_playwright
import re


with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.sympla.com.br/produtor/digitalcollegebr')
        python_imgs_locator = page.get_by_role("link", name=re.compile("python", re.IGNORECASE)).locator("img")
        python_srcs = python_imgs_locator.evaluate_all("elements => elements.map(e => e.src)")
        print(python_srcs)