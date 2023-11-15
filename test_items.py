import selenium.webdriver.common.by
import pytest
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_page_item_button_is_visible(browser):
    browser.get(link)
    assert len(browser.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR, '.btn-add-to-basket')) > 0
