from Emag.Category import Category
from Emag.PageTimer import Timer
import threading

try:
    category = Category()
    category.get_category('https://www.emag.ro/desktop-pc/c?ref=hp_menu_quick-nav_23_1&type=category')
    category.get_category('https://www.emag.ro/laptopuri/c')
    category.get_category('https://www.emag.ro/placi_video/c?ref=effective_search')
    category.get_category('https://www.emag.ro/memorii/c?ref=effective_search')
    del category

    timer = Timer()

    timer.timer_('https://www.emag.ro/laptopuri/c?ref=effective_search', 26, 'https://www.emag.ro/laptopuri')
    timer.timer_('https://www.emag.ro/desktop-pc/c?ref=effective_search', 246, 'https://www.emag.ro/desktop-pc')
    timer.timer_('https://www.emag.ro/placi_video/c?ref=effective_search', 12, 'https://www.emag.ro/placi_video')
    timer.timer_('https://www.emag.ro/memorii/c?ref=effective_search', 28, 'https://www.emag.ro/memorii')

    del timer
except Exception as e:
    print(f'ERROR - {e}')