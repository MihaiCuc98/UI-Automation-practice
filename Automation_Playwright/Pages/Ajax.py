from playwright.sync_api import expect, Page
import time

class Ajax:
    def __init__(self, page: Page):
        self.page = page
        self.button_locator = page.locator('xpath=//button[@id="ajaxButton"]')
        self.response = page.locator('xpath=//p[text()="Data loaded with AJAX get request."]')

    def element_appear(self):
        self.button_locator.click()
        self.page.wait_for_selector('xpath=//p[text()="Data loaded with AJAX get request."]', state="visible")
        return self.response.is_visible()


