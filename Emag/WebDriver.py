from selenium import webdriver


# Initialization selenium
class Initialization(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.emag.ro/')
        self.driver.refresh()


