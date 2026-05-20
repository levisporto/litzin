import streamlit as st
from playwright.sync_api import sync_playwright
import os

# Force Playwright to install the Chromium binary on the cloud server
os.system("playwright install chromium")
os.system("playwright install-deps chromium")

def run_scraper(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        all_text = page.inner_text('body')
        browser.close()
        return all_text

st.title("Streamlit + Playwright Scraper")

if st.button("Scrape"):
    result = run_scraper('https://www.sympla.com.br/produtor/digitalcollegebr')
    st.write(f"Page Title: {result}")
