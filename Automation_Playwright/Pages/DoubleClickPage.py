from playwright.sync_api import Page


class DoubleClickPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn_success = page.locator('xpath = //button[@class = "btn btn-success"]')

    def double_click(self):
        self.btn_success.click()
        self.btn_success.click()