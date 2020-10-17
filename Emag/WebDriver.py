from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# Initialization selenium
class Initialization(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Users\\NaiTuTreaba\\PycharmProjects\\AliExpress\\chromedriver.exe')
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)