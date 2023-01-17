import time
from selenium.webdriver import ActionChains
from pages.locators import TypeManualSearchCheckboxes


class SortManualAttr():
    """Класс для работы с основными кнопками сортировки"""

    def __init__(self, browser):
        """Инициализация ключевых атрибутов класса"""
        self.browser = browser

    # get elements

    def get_manual_apple_checkbox(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.MANUFACTURER_TYPE_APPLE)

    def get_manual_notebook_checkbox(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.TYPE_DEVICE_NOTEBOOK)

    def get_manual_cpu_type_checkbox(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.CPU_TYPE)

    def get_manual_golden_color_device_checkbox(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.GOLDEN_COLOR_DEVICE)

    def get_first_position_device_in_sort_list(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.TOP_IN_SORT_LIST_DEVICE_IMG)

    def get_fast_delivery_button_in_sort_list(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.SORT_DELIVERY_TODAY)

    def get_16_bg_ram_checkbox(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.RAM_16_GB_SELECT_BUTTON)

    def get_all_categories_link_button(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.ALL_CATEGORIES_BUTTON)

    def get_phones_and_gadgets_category(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.CATEGORY_PHONES_AND_GADGETS)

    def get_smartphones_category_button(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.CATEGORY_SMARTPHONES)

    def get_apple_img(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.APPLE_IMG)

    def get_iphone_14_pro_max_checkbox(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.IPHONE_14_PRO_MAX)

    def get_manual_purple_color_device_checkbox(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.PURPLE_COLOR_DEVICE)

    # actions

    def choice_manufacturer_apple_checkbox(self):
        time.sleep(1)
        self.get_manual_apple_checkbox().click()
        time.sleep(1)
        print("\nPICK SETUP:")
        print("apple")

    def choice_device_type_notebook_checkbox(self):
        time.sleep(2)
        self.get_manual_notebook_checkbox().click()
        print("notebook")

    def choice_apple_m1_cpu_checkbox(self):
        time.sleep(2)
        self.get_manual_cpu_type_checkbox().click()
        print("apple m1")

    def choice_golden_color_device_checkbox(self):
        time.sleep(2)
        self.get_manual_golden_color_device_checkbox().click()

    def click_to_top_device_in_sort_list(self):
        time.sleep(2.5)
        self.get_first_position_device_in_sort_list().click()

    def choice_delivery_today_checkbox(self):
        time.sleep(2)
        self.get_fast_delivery_button_in_sort_list().click()
        print("fast delivery")

    def choice_16_gb_ram_checkbox(self):
        time.sleep(2)
        self.get_16_bg_ram_checkbox().click()
        print("16 GB RAM")

    def hover_to_button_or_link(self, needed_element):
        hover_element = ActionChains(self.browser)
        hover_element.move_to_element(needed_element)
        hover_element.perform()
        time.sleep(1)

    def click_smartphones_button(self):
        self.get_smartphones_category_button().click()

    def click_to_apple_img_in_list(self):
        self.get_apple_img().click()
        time.sleep(2)

    def choice_iphone_14_pro_max_checkbox(self):
        self.get_iphone_14_pro_max_checkbox().click()
        print("\nPIK SETUP:\n")
        time.sleep(2)
        print("iPhone 14 pro max")


    def choice_purple_color_device_checkbox(self):
        self.get_manual_purple_color_device_checkbox().click()
        print("color purple")
        time.sleep(2)

    # methods

    def use_setup_apple_notebook_apple_m1_golden(self):
        self.choice_manufacturer_apple_checkbox()
        self.choice_apple_m1_cpu_checkbox()
        self.choice_golden_color_device_checkbox()
        self.choice_device_type_notebook_checkbox()
        self.click_to_top_device_in_sort_list()

    def use_setup_macbook_pro_16_gb_ram_delivery_today(self):
        self.choice_manufacturer_apple_checkbox()
        self.choice_delivery_today_checkbox()
        self.choice_device_type_notebook_checkbox()
        self.choice_16_gb_ram_checkbox()
        self.click_to_top_device_in_sort_list()

    def use_setup_top_purple_iphone_14_pro_max(self):
        self.hover_to_button_or_link(self.get_all_categories_link_button())
        self.hover_to_button_or_link(self.get_phones_and_gadgets_category())
        self.click_smartphones_button()
        self.click_to_apple_img_in_list()
        self.choice_iphone_14_pro_max_checkbox()
        self.choice_purple_color_device_checkbox()
