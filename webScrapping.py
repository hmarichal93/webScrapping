#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 15:50:53 2020

@author: henry
"""
# import requests

# ##URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)

# pagina = page.content

# #%%
# paginaString = pagina.decode("utf-8")


# #%%

# with open("Contenido.txt", "w") as text_file:
#     text_file.write(paginaString)

# from requests_html import HTMLSession
# session = HTMLSession()

# r = session.get(URL)

import requests
from requests_html import HTMLSession
 
#url = "https://www.searchenginejournal.com/introduction-to-python-seo-spreadsheets/342779/"
URL = 'https://ventas.turismar.com.uy/reserva-en-linea.php'
 
try:
    session = HTMLSession()
    response = session.get(URL)
    about = response.html.find('script', first=True)
except requests.exceptions.RequestException as e:
    print(e)