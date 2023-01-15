import time

from pages.chek_result_parameters import CheckResultParametersNoteebok
from pages.main_page import MainPage
from pages.sort_manual_attributes import SortManualAttr


def test_buy_most_expensive_golden_macbook_air_m1_from_global_search(browser):
    main_page = MainPage(browser)
    main_page.find_and_input_search_parameters("macbook air m1")
    main_page.choice_sort_by_price()
    sort_parameters = SortManualAttr(browser)
    sort_parameters.use_setup_apple_notebook_apple_m1_golden()
    check_parameters = CheckResultParametersNoteebok(browser)
    check_parameters.check_product_code_is_exist()
    check_parameters.check_selected_product_contain_key_phrases(['macbook', 'air'])
    main_page.screenshot_page('golden_MacBook_air')






