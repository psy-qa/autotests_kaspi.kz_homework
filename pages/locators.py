from selenium.webdriver.common.by import By


class ForManualSearchPageLocators():
    """Описание используемых локаторов длс стартовой страницы"""
    SEARCH_BAR_INPUT = (By.XPATH, "//input[@class='search-bar__input']")
    SEARCH_BAR_BUTTON = (By.XPATH, "//button[@class='search-bar__submit button']")
    CONFIRM_LOCATION_BUTTON = (By.XPATH, "//button[@id='current-location-yes']")
    SORT_BUTTON = (By.XPATH, "//div[@class='select__title']")
    SORT_PRICE_UP_BUTTON = (By.XPATH, "//*[@data-raw-value='price-desc']")
    SORT_PRICE_DOWN_BUTTON = (By.XPATH, "//*[@data-raw-value='price-asc']")
    BUTTON_TO_GENERATE_QR = (By.XPATH, "//button[text()='Открыть в приложении Kaspi.kz']")
    SORT_HIGH_RATING = (By.XPATH, "//li[text() = 'Высокий рейтинг']")
    # INFO_ABOUT_REVIEW = (By.XPATH, "//div[@class='item-card__rating']/a[contains(text(),'отзыв')]")



class TypeManualSearchCheckboxes():

    """Описание используемых локаторов для сортировки по нужным параметрам"""
    MANUFACTURER_TYPE_APPLE = (By.XPATH, "//span[text() = 'Apple']")
    TYPE_DEVICE_NOTEBOOK = (By.XPATH, "//span[text() = 'ноутбук']")
    CPU_TYPE = (By.XPATH, "//span[text() = 'Apple M1']")
    GOLDEN_COLOR_DEVICE = (By.XPATH, "//span[text() = 'золотистый']")
    TOP_IN_SORT_LIST_DEVICE_IMG = (By.XPATH, "//div[@class='item-cards-grid__cards']/div[1]/a/img")
    SORT_DELIVERY_TODAY = (By.XPATH, "//*[text()='Сегодня']")
    RAM_16_GB_SELECT_BUTTON = (By.XPATH, "//*[text()='16 Гб']")
    ALL_CATEGORIES_BUTTON = (By.XPATH, "//*[text() = 'Все категории']")
    CATEGORY_PHONES_AND_GADGETS = (By.XPATH, "//*[text() = 'Телефоны и гаджеты']")
    CATEGORY_SMARTPHONES = (By.XPATH, "//*[text() = 'Смартфоны']")
    APPLE_IMG = (By.XPATH, "//span/img[contains(@src,'apple')]")
    IPHONE_14_PRO_MAX = (By.XPATH, "//span[text() = 'Apple iPhone 14 Pro Max']")
    PURPLE_COLOR_DEVICE = (By.XPATH, "//span[text() = 'фиолетовый']")

class CheckSelectedProduct():
    """Описание использвуемых локаторов для проверки выбранных устройств"""
    PRODUCT_CODE_SELECTED_DEVICE = (By.XPATH, "//div[@class='item__sku']")
    PRODUCT_TITLE_SELECTED_DEVICE = (By.XPATH, "//*[@class='item__heading']")
    PRODUCT_SELECTED_SPECIFICATIONS = (By.XPATH, "//*[@data-tab = 'specifications']")
