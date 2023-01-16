import time

from pages.chek_result_parameters import CheckResultParametersNoteebok
from pages.main_page import MainPage
from pages.sort_manual_attributes import SortManualAttr


def test_buy_most_expensive_golden_macbook_air_m1_from_global_search(browser):
    main_page = MainPage(browser)
    main_page.find_and_input_search_parameters("macbook air m1")
    main_page.choice_sort_by_price_up()
    sort_parameters = SortManualAttr(browser)
    sort_parameters.use_setup_apple_notebook_apple_m1_golden()
    check_parameters = CheckResultParametersNoteebok(browser)
    check_parameters.check_product_code_is_exist()
    check_parameters.check_selected_product_contain_key_phrases(['macbook', 'air'])
    check_parameters.check_specifications_parameters_in_page(['ноутбук', 'apple m1', 'золотистый'])
    main_page.screenshot_page('golden_MacBook_air')
    main_page.click_button_to_generate_qr()
    main_page.screenshot_qr('golden_Macbook_air_QR')


def test_buy_macbook_m1_cheap_and_fast_delivery(browser):
    main_page = MainPage(browser)
    main_page.find_and_input_search_parameters("macbook pro m1")
    main_page.choice_sort_by_price_down()
    sort_parameters = SortManualAttr(browser)
    sort_parameters.use_setup_macbook_pro_16_gb_ram_delivery_today()
    check_parameters = CheckResultParametersNoteebok(browser)
    check_parameters.check_product_code_is_exist()
    check_parameters.check_selected_product_contain_key_phrases(["macbook", 'pro'])
    check_parameters.check_specifications_parameters_in_page(['ноутбук', '16 гб'])
    main_page.screenshot_page('cheap_macbook_pro_16gb')
    main_page.click_button_to_generate_qr()
    main_page.screenshot_qr('cheap_macbook_pro_16gb_QR')


def test_buy_top_purple_iphone_14_pro_max_for_best_review(browser):
    pass
