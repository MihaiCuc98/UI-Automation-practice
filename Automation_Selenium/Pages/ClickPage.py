import time

from selenium.webdriver.common.by import By
class ClickPage:
    button_xpath = '//button[contains(text(),"Button That Ignores DOM Click Event")]'


    def __init__(self, browser):
        self.browser = browser

    def get_click_button(self):
        return self.browser.find_element(By.XPATH, self.button_xpath)

    def click_button(self):
        element = self.browser.find_element(By.XPATH, self.button_xpath)
        element.click()

    def get_class_button(self):
        element = self.browser.find_element(By.XPATH, self.button_xpath)
        return element.get_attribute('class')