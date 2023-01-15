from pages.locators import CheckSelectedProduct


class CheckResultParametersNoteebok():
    """Класс для сравнения выбранного ноутбука и его параметров пр сортировке"""

    def __init__(self,browser):
        """Инициализация ключевых атрибутов класса"""
        self.browser = browser

    # get elements

    def get_selected_product_code(self):
        return self.browser.find_element(*CheckSelectedProduct.PRODUCT_CODE_SELECTED_DEVICE)
    def get_selected_device_title(self):
        return self.browser.find_element(*CheckSelectedProduct.PRODUCT_TITLE_SELECTED_DEVICE)

    # actions

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
