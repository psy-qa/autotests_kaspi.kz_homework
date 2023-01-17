from selenium.webdriver.common.by import By
from pages.locators import CheckSelectedProduct


class CheckResultParametersNoteebok():
    """Класс для сравнения выбранного ноутбука и его параметров пр сортировке"""

    def __init__(self, browser):
        """Инициализация ключевых атрибутов класса"""
        self.browser = browser

    # get elements

    def get_selected_product_code(self):
        return self.browser.find_element(*CheckSelectedProduct.PRODUCT_CODE_SELECTED_DEVICE)

    def get_selected_device_title(self):
        return self.browser.find_element(*CheckSelectedProduct.PRODUCT_TITLE_SELECTED_DEVICE)

    def get_product_specification_button(self):
        return self.browser.find_element(*CheckSelectedProduct.PRODUCT_SELECTED_SPECIFICATIONS)

    def get_specification_parameters(self, parameter):
        return self.browser.find_element(By.XPATH, f"//*[@class = 'specifications-list ']/*/dd/*/dd[text()"
                                                   f"='{parameter}']")

    # actions

    def click_specification_button(self):
        self.get_product_specification_button().click()

    # methods

    def check_product_code_is_exist(self):
        if self.get_selected_product_code():
            product_code_string = self.get_selected_product_code().text
            product_code = product_code_string[12:]
            print(f"Product code selected device = {product_code}")

    def check_selected_product_contain_key_phrases(self, product_title_words):
        if self.get_selected_device_title():
            product_title_string = self.get_selected_device_title().text
            if type(product_title_words) == str:
                assert product_title_words.lower() in product_title_string.lower()
            elif type(product_title_words) == list:
                for search_word in product_title_words:
                    assert search_word.lower() in product_title_string.lower()
            else:
                print("Wrong request")

    def check_specification_contain_parameters_in_page(self, parameters):
        # ноутбук/Aplle M1/золотистый
        # ноутбук/16 ГБ

        if type(parameters) == str:
            if parameters == 'apple m1':
                parameters = parameters.title()
            elif parameters == '16 гб':
                parameters = parameters.upper()
            else:
                parameters = parameters.lower()
            assert self.get_specification_parameters(parameters), "Wrong parameter title"

        elif type(parameters) == list:
            for parameter in parameters:
                if parameter == 'apple m1':
                    parameter = parameter.title()
                elif parameter == '16 гб':
                    parameter = parameter.upper()
                else:
                    parameter = parameter.lower()
                assert self.get_specification_parameters(parameter), "Wrong parameters title"
