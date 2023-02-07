
class ClickPage:
    URL = 'http://uitestingplayground.com/'

    def __init__(self, page):
        self.page = page
        self.click_page_link = page.locator('xpath=//button[contains(text(),"Button")]')

    def load(self):
        self.page.goto(self.URL)

    def click_button(self):
        self.click_page_link.click()

