import streamlit as st
from playwright.sync_api import sync_playwright
import re

def run_scraper(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        todos_os_eventos = page.locator('a').all_inner_texts() 
        browser.close()
        return todos_os_eventos

st.title("Digital College - Eventos Data Analytics")
result = run_scraper('https://www.sympla.com.br/produtor/digitalcollegebr')

busca = re.compile(r"dados|python|analista|análise|data|analysis|analyst", re.IGNORECASE)

for resultados in result:
    if busca.search(resultados):
        st.write(f"{resultados}")
    
