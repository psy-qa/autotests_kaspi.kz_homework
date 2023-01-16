import datetime
import time

from pages.locators import ForManualSearchPageLocators


class MainPage():
    """Класс для работы с основной страницей поиска товаров"""

    def __init__(self, browser):
        """Иницализация ключевых атрибутов класса"""
        self.browser = browser

    # get elements

    def get_alert_locations(self):
        return self.browser.find_element(*ForManualSearchPageLocators.CONFIRM_LOCATION_BUTTON)

    def get_search_bar(self):
        return self.browser.find_element(*ForManualSearchPageLocators.SEARCH_BAR_INPUT)

    def get_search_button(self):
        return self.browser.find_element(*ForManualSearchPageLocators.SEARCH_BAR_BUTTON)

    def get_sort_list_button(self):
        return self.browser.find_element(*ForManualSearchPageLocators.SORT_BUTTON)

    def get_sort_by_price_up_button(self):
        return self.browser.find_element(*ForManualSearchPageLocators.SORT_PRICE_UP_BUTTON)

    def get_sort_by_price_down_button(self):
        return self.browser.find_element(*ForManualSearchPageLocators.SORT_PRICE_DOWN_BUTTON)

    def get_button_for_generate_qr_code(self):
        return self.browser.find_element(*ForManualSearchPageLocators.BUTTON_TO_GENRATE_QR)

    # actions

    def skip_location_alert(self):
        self.get_alert_locations().click()

    def input_search_bar(self, search_parameter):
        self.get_search_bar().send_keys(search_parameter)

    def click_search_button(self):
        self.get_search_button().click()

    def click_sort_button(self):
        self.get_sort_list_button().click()

    def click_sort_by_price_up_button(self):
        self.get_sort_by_price_up_button().click()

    def click_sort_by_price_down_button(self):
        self.get_sort_by_price_down_button().click()

    def click_button_to_generate_qr(self):
        self.get_button_for_generate_qr_code().click()
        print("click to generate qr")
        time.sleep(2)

    def screenshot_page(self, selected_product):
        now_date = datetime.datetime.utcnow().strftime("%d_%B_%Y_%H-%M-%S")
        name_screenshot = f'screenshot_{selected_product}({now_date}).png'
        self.browser.save_screenshot(f"../screenshots/{name_screenshot}")
        print(f"Saved screenshot {selected_product} in screenshots page")

    def screenshot_qr(self, selected_product):
        now_date = datetime.datetime.utcnow().strftime("%d_%B_%Y_%H-%M-%S")
        name_screenshot = f'screenshot_{selected_product}({now_date}).png'
        self.browser.save_screenshot(f"../screenshots/qr/{name_screenshot}")
        print(f"Saved screenshot QR {selected_product} in screenshots/qr page")

    # methods

    def find_and_input_search_parameters(self, search_parameter):
        self.skip_location_alert()
        self.input_search_bar(search_parameter)
        self.click_search_button()

    def choice_sort_by_price_up(self):
        self.click_sort_button()
        self.click_sort_by_price_up_button()

    def choice_sort_by_price_down(self):
        self.click_sort_button()
        self.click_sort_by_price_down_button()

