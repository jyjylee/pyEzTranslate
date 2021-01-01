from google_trans_new import google_translator
from requests_file import FileAdapter
from bs4 import BeautifulSoup as bs
import requests

class smartling:
    '''
        Using requests/requests_file to get html for
    '''
    def __init__(self, url='', local=False):
        if local==True:
            self.s.mount('file://', FileAdapter())
            html = self.s.get('file:///'+url)
        else:
            html=requests(url)
        self.soup = bs(html.text, 'html.parser').find(class_="stringsList__performanceBooster___2P0aYE")

    def crawling(self):
        for i in range(30):
            line_id = 'js-scroll-' + str(i)
            # source(번역대상)와 target(번역입력)으로 나뉘어 있음, 여기서는 번역대상만을 가져와서 그중에 데이터만 긁음
            # 나중에 번역이 일부 되어있는 번역본의 경우에 그 파트는 건너뛰게 하거나 긁어서 다른쪽으로 미리 넣거나 무시할 수 있도록 해야할 듯
            text = self.soup.find(id=line_id).find(class_="segments__source___2Vmtne").find_all('span',
                                                                                           {"data-text": "true"})
            sum = ""
            for element in text:
                sum += str(element.string)
                if element == "":
                    break
            print(sum)

    def translate(self):
        translator = google_translator()
        result = translator.translate(sum, lang_tgt='ko')

