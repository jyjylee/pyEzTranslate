import os
import requests
from requests_file import FileAdapter
from bs4 import BeautifulSoup as bs

s = requests.Session()
s.mount('file://', FileAdapter())

html = s.get('file:///C:/Users/dlwld/PycharmProjects/pyEzTranslate/Smartling.html')

soup=bs(html.text,'html.parser')

print(soup)