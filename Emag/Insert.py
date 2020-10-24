from Emag.Category import Category
from Emag.PageTimer import Timer
import threading

# category = Category()
# category.get_category('https://www.emag.ro/desktop-pc/c?ref=hp_menu_quick-nav_23_1&type=category')
# category.get_category('https://www.emag.ro/laptopuri/c')
# del category

timer = Timer()
th1 = threading.Thread(target=timer.timer_, args=('https://www.emag.ro/laptopuri/c?ref=effective_search', 26, 'https://www.emag.ro/laptopuri',))
th2 = threading.Thread(target=timer.timer_, args=('https://www.emag.ro/desktop-pc/c?ref=effective_search', 246, 'https://www.emag.ro/desktop-pc',))

th1.start()
th2.start()

del timer
