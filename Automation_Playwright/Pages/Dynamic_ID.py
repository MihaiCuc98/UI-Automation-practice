from playwright.sync_api import Page


class Dynamic_ID:
    def __init__(self, page: Page):
        self.page = page
        self.button = page.locator('//button[contains(text(),"Button with Dynamic ID")]')

    def click_button(self):
        self.button.click()
