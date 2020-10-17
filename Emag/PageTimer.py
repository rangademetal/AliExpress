from Emag.WebDriver import Initialization
import time


start = time.perf_counter()
emag = Initialization()
source = 'https://www.emag.ro/search/laptopuri/laptop/c?ref=autosuggest_category1'
emag.driver.get(source)
stop = time.perf_counter()
print(f'Loading selenium: {stop-start:0.4f} secounds')
total = []
for i in range(1, 29):
    start = time.perf_counter()
    emag.driver.get(f'https://www.emag.ro/search/laptopuri/laptop/p{i}/c')
    stop = time.perf_counter()
    timer = f'{stop - start:0.4f}'
    timer = float(timer)
    total.append(timer)
    print(f'Page {emag.driver.current_url} have {stop - start:0.4f} seconds')
print(f'Total loading time is: {sum(map(float, total))}')
