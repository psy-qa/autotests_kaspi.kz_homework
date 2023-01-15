import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    print("\nStart test")
    browser = webdriver.Chrome()
    browser.get("https://kaspi.kz/shop/aktau")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print("\nFinish test")


