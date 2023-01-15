import time

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

    def get_manual_cpu_type(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.CPU_TYPE)

    def get_manual_golden_color_device(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.GOLDEN_COLOR_DEVICE)

    def get_first_position_device_in_sort_list(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.TOP_IN_SORT_LIST_DEVICE_IMG)

    # actions

    def choice_manufacturer_apple(self):
        self.get_manual_apple_checkbox().click()
        print("\nSETUP:")
        print("apple")

    def choice_device_type_notebook(self):
        self.get_manual_notebook_checkbox().click()
        print("notebook")

    def choice_apple_m1_cpu(self):
        self.get_manual_cpu_type().click()
        print("apple m1")

    def choice_golden_color_device(self):
        self.get_manual_golden_color_device().click()
        print('golden')

    def click_to_top_device_in_sort_list(self):
        self.get_first_position_device_in_sort_list().click()

    # methods
    def use_setup_apple_notebook_apple_m1_golden(self):
        self.choice_manufacturer_apple()
        self.choice_golden_color_device()
        self.choice_device_type_notebook()
        self.choice_apple_m1_cpu()
        self.click_to_top_device_in_sort_list()


