from playwright.sync_api import expect, Page

class ProgressBar:
    def __init__(self, page: Page):
        self.page = page
        self.start_button = page.locator('xpath=//button[contains(text(),"Start")]')
        self.stop_button = page.locator('xpath=//button[contains(text(),"Stop")]')

    def progressbar(self, nr: str):
        locator = self.page.locator('xpath=//div[contains(text(),"' + nr + '%'+'")]')
        return locator

    def start(self):
        self.start_button.click()

    def stop(self):
        for x in range(100):
            y = str(x)
            if self.progressbar(y) is True:
                self.stop_button.click()
                break
