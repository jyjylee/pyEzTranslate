import os
import requests
from requests_file import FileAdapter
from bs4 import BeautifulSoup as bs
from google_trans_new import google_translator

#Local Test session
s = requests.Session()
s.mount('file://', FileAdapter())
html = s.get('file:///C:/Users/dlwld/PycharmProjects/pyEzTranslate/Smartling.html')
soup=bs(html.text,'html.parser')

#전체 번역 Contents를 찾고
soup=soup.find(class_="stringsList__performanceBooster___2P0aYE")
for i in range(30):
    line_id='js-scroll-'+str(i)
    #source(번역대상)와 target(번역입력)으로 나뉘어 있음, 여기서는 번역대상만을 가져와서 그중에 데이터만 긁음
    #나중에 번역이 일부 되어있는 번역본의 경우에 그 파트는 건너뛰게 하거나 긁어서 다른쪽으로 미리 넣거나 무시할 수 있도록 해야할 듯
    text=soup.find(id=line_id).find(class_="segments__source___2Vmtne").find_all('span', {"data-text": "true"})
    sum=""
    for element in text:
        sum+=str(element.string)
        if element=="":
            break
    print(sum)
    translator = google_translator()
    result = translator.translate(sum, lang_tgt='ko')
    print(result)