from selenium.webdriver.common.by import By


class MainPage:
    click_page_locator = '//a[contains(text(),"Click")]'
    URL = 'http://uitestingplayground.com/'

    def __init__(self, browser):
        self.browser = browser

    def get_click_page(self):
        return self.browser.find_element(By.XPATH, self.click_page_locator)

    def click_click_page(self):
        self.browser.execute_script("arguments[0].click();", self.get_click_page())

    def load_page(self):
        self.browser.get(self.URL)
