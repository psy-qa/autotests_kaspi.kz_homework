import datetime
import re
import time
from selenium.webdriver.common.by import By
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
        return self.browser.find_element(*ForManualSearchPageLocators.BUTTON_TO_GENERATE_QR)

    def get_sort_by_high_rating_button_link(self):
        return self.browser.find_element(*ForManualSearchPageLocators.SORT_HIGH_RATING)

    def get_element_contain_number_of_review(self, number):
        return self.browser.find_element(By.XPATH, f"//div[@class='item-cards-grid__cards']/div[{number}]"
                                                   f"/div[@class = 'item-card__info']/"
                                                   f"div[@class= 'item-card__rating']/a")

    def get_number_element_of_max_review(self):
        return self.sort_device_in_list_devices_max_review_number('max')

    def get_element_after_sorting_of_max_review(self):
        number_element_in_list = self.get_number_element_of_max_review()
        return self.browser.find_element(By.XPATH, f"//div[@class='item-cards-grid__cards']/div[{number_element_in_list}]/div[2]/div[1]/a")

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

    def click_sort_by_high_rating(self):
        self.get_sort_by_high_rating_button_link().click()

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

    def sort_device_in_list_devices_max_review_number(self, max_or_min):
        # метод для поиска максимального\минимального кол-ва отзывов
        list_items = []
        list_items_int = []
        try:
            # получим отображаемый контейнеры с товарами
            for number in range(1, 99):
                element = self.get_element_contain_number_of_review(number).text
                list_items.append(element)
        except:
            # если их меньше 99, скрипаем все ок
            pass
        for item in list_items:
            # вычленяем из элементов полученного списка только цифры
            only_numbers = re.findall(r'\d+', item)
            # создаем новый список, элементами которого будут целые числа
            list_items_int.append(int(only_numbers[0]))
        if max_or_min == 'max':
            #выберем максимальное и минимальное кол-во из списка
            top_review_int = max(list_items_int)
        elif max_or_min == 'min':
            top_review_int = min(list_items_int)
        # вернем номер контейнера с товаром
        result_sort_index = list_items_int.index(top_review_int) + 1
        return result_sort_index

    def click_element_after_sorting_of_max_review(self):
        self.get_element_after_sorting_of_max_review().click()

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

    def choice_sort_by_high_rating(self):
        time.sleep(1)
        self.click_sort_button()
        time.sleep(1)
        self.click_sort_by_high_rating()
        time.sleep(2)
        self.click_element_after_sorting_of_max_review()
