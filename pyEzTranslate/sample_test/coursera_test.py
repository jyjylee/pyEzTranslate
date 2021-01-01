import requests
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome import webdriver
from selenium.webdriver import ActionChains
from selenium import webdriver
import yaml
from selenium.webdriver.common.keys import Keys

URL="https://www.coursera.org/?authMode=login"
with open('config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

with open('xpathlist.yml') as f:
    xpath= yaml.load(f, loader=yaml.FullLoader)

with open('web.yml') as f:
    web= yaml.load(f, loader=yaml.FullLoader)

email = config['UserName']
password = config['Password']

print(email)
print(password)


driver=webdriver.Chrome(config['chromedriverPath'])
driver.get(web['coursera_login'])
time.sleep(3)

# Click GMail login
driver.find_element_by_xpath(xpath['gmail_login_button']).click()

time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])

email_field = driver.find_element_by_name("identifier")
email_field.send_keys(email)
email_next_btn=driver.find_element_by_xpath(xpath['gmail_next_button'])
email_next_btn.click()
time.sleep(2)

password_field = driver.find_element_by_name("password")
password_field.send_keys(password)
password_next_btn=driver.find_element_by_xpath(xpath['gmail_next_button'])
password_next_btn.click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[0])
driver.get_window_position(driver.window_handles[0])
time.sleep(5)

driver.get(web['translate_coursera'])
get_in_btn=driver.find_element_by_xpath(xpath['get_in_button'])
get_in_btn.click()

driver.get(web['translate_coursera_course'])

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 999)
element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath['translate_search_edit'])))

class_name="Deep Neural Networks with PyTorch"
search=driver.find_element_by_xpath(xpath['translate_search_edit'])
search.send_keys(class_name)
time.sleep(2)
driver.find_element_by_xpath("/html/body/span/div/div/div[2]/div[2]/span/div[3]/div/div/div/div[2]/div[2]/table/tbody/tr/td[8]/a").click()

#몇 번쨰?

a=input("몇 번째 영상을 번역하시겠습니까: ")
xpath_for_translate="//*[@id='page-wrapper']/div[2]/span/div[2]/div[1]/div/div/div/div[4]/div/div/uib-tabset/uib-tab/table/tbody/tr["+a+"]/td[4]/a"
driver.find_element_by_xpath(xpath_for_translate).click()


##1번째 것의 translate 하이퍼링크의 xPath
##//*[@id="page-wrapper"]/div[2]/span/div[2]/div[1]/div/div/div/div[4]/div/div/uib-tabset/uib-tab/table/tbody/tr[1]/td[4]/a
##3번째 것의 translate 하이퍼링크의 xPath
##//*[@id="page-wrapper"]/div[2]/span/div[2]/div[1]/div/div/div/div[4]/div/div/uib-tabset/uib-tab/table/tbody/tr[3]/td[4]/a
##따라서 tr의 값만 다름 1에서 시작

## wait for opening the translate window

## shift to smartling windows
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])

##SOL
## find how long the text cells are

## Start scraping a line to here
i=1
html=requests(driver.current_url)
soup=bs(html,'html.parser')

rotate=driver.find_element_by_xpath("//*[@id='js-scroll-0-0-1']/div/div[1]/div/div/div/div/div/div/div/div/span["+i+"]")
rotate==True


## Translate the scraped sentence

##(Optional) Change the translated one with following the rules

## Save the translated sentense

##EOL
exit()

translator=Translator()
result=translator.translate('Hello my friend',dest="ko")
print(result.text)