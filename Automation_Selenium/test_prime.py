import time
import pytest
from selenium.webdriver import Chrome
from Pages.ClickPage import ClickPage
from Pages.MainPage import MainPage

button_class = "btn btn-success"


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_click(browser):
    click_page = ClickPage(browser)
    main_page = MainPage(browser)
    main_page.load_page()
    time.sleep(2)
    main_page.click_click_page()
    time.sleep(5)
    click_page.click_button()
    time.sleep(2)
    assert click_page.get_class_button() == button_class



