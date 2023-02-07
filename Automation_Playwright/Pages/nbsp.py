from playwright.sync_api import Page

class nbsp:
    def __init__(self, page: Page):
        self.page = page
        self.button_locator = page.locator('xpath=//button[contains(text(),"My&nbsp;Button")]')

    def click_button(self):
        self.button_locator.click()
