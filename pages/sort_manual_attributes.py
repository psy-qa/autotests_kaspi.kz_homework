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

    def get_fast_delivery_button_in_sort_list(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.SORT_DELIVERY_TODAY)

    def get_16_bg_ram_button(self):
        return self.browser.find_element(*TypeManualSearchCheckboxes.RAM_16_GB_SELECT_BUTTON)

    # actions

    def choice_manufacturer_apple(self):
        time.sleep(1)
        self.get_manual_apple_checkbox().click()
        time.sleep(1)
        print("\nPICK SETUP:")
        print("apple")

    def choice_device_type_notebook(self):
        time.sleep(2)
        self.get_manual_notebook_checkbox().click()
        print("notebook")

    def choice_apple_m1_cpu(self):
        time.sleep(2)
        self.get_manual_cpu_type().click()
        print("apple m1")

    def choice_golden_color_device(self):
        time.sleep(2)
        self.get_manual_golden_color_device().click()
        print('golden')

    def click_to_top_device_in_sort_list(self):
        time.sleep(2.5)
        self.get_first_position_device_in_sort_list().click()

    def choice_delivery_today_checkbox(self):
        time.sleep(2)
        self.get_fast_delivery_button_in_sort_list().click()
        print("fast delivery")

    def choice_16_gb_ram_checkbox(self):
        time.sleep(2)
        self.get_16_bg_ram_button().click()
        print("16 GB RAM")

    # methods

    def use_setup_apple_notebook_apple_m1_golden(self):
        self.choice_manufacturer_apple()
        self.choice_golden_color_device()
        self.choice_apple_m1_cpu()
        self.choice_device_type_notebook()
        self.click_to_top_device_in_sort_list()

    def use_setup_macbook_pro_16_gb_ram_delivery_today(self):
        self.choice_manufacturer_apple()
        self.choice_delivery_today_checkbox()
        self.choice_device_type_notebook()
        self.choice_16_gb_ram_checkbox()
        self.click_to_top_device_in_sort_list()



