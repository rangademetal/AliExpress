from Database.Secret import *
from Database.ConnectionDatabase import ConnectionDatabase
from Emag.WebDriver import Initialization
from selenium.common.exceptions import NoSuchElementException
import time

scanner = Initialization()
database = ConnectionDatabase(DB_DATABASE)

scanner.driver.get('https://www.emag.ro/laptopuri/c?ref=effective_search')

count = 1
scroll = 0

while count != 62:
    scanner.driver.execute_script('window.scrollTo(0, ' + str(scroll) + ')')
    print(count)
    try:
        clickers = scanner.driver.find_element_by_xpath(f'//*[@id="card_grid"]/div[{count}]/div/div/div[2]/h2/a')
    except NoSuchElementException as e:
        continue

    start = time.perf_counter()
    clickers.click()
    stop = time.perf_counter()
    count += 1
    if count % 5 == 0:
        count += 1

    scroll += 145
    timer = f'{stop - start:0.4f}'
    timer = float(timer)
    print(timer)
    scanner.driver.execute_script("window.history.go(-1)")
    time.sleep(1)