import yaml
from selenium import webdriver

class coursera_util:
    def __init__(self):
        with open('../yml_file/config.yml') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        with open('../yml_file/xpathlist.yml') as f:
            xpath = yaml.load(f, loader=yaml.FullLoader)

        email = config['UserName']
        password = config['Password']

    def driver_on(self, chrome=True):
        driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        driver.get("https://www.coursera.org/?authMode=login")

    def google_login(self):
        pass

    def