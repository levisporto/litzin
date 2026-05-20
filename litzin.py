import streamlit as st
from playwright.sync_api import sync_playwright
import re

st.title("Digital College - Eventos Data Analytics")


with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.sympla.com.br/produtor/digitalcollegebr')
        todos_os_eventos = page.locator('a').all_inner_texts() 
        links_locator = page.locator("a")
        all_links = links_locator.evaluate_all("elements => elements.map(e => e.href)")
        busca = re.compile(r"dados|python|analista|análise|data|analysis|analyst", re.IGNORECASE)
        evento_list = []
        link_list = []

        for resultados in todos_os_eventos:
            if busca.search(resultados):
                evento_list.append(resultados)
        

        for resultados in all_links:
            if busca.search(resultados):
                link_list.append(resultados)
            
        for evento, link in zip(evento_list, link_list):
            st.subheader(f"📅 {evento}")
            st.write(f"Link: {link}")
            st.write("---") # Optional: adds a line between results
                
        
        
        browser.close()
        
        




    
