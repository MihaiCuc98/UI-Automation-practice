from playwright.sync_api import Page


class VerifyText:
    def __init__(self, page: Page):
        self.page = page
        self.welcome_text = page.locator('//span[1][normalize-space(.)="Welcome UserName!"]')

    def return_text(self):
        return self.welcome_text.is_visible()
