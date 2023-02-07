from playwright.sync_api import expect, Page

class DynamicTable:
    def __init__(self, page: Page):
        self.page = page
        self.percent_chrome_locator = self.page.locator('xpath=//span[contains(text(),"Chrome")]/.././*[contains(text(),"%")]')
        self.orange = self.page.locator('xpath=//p[@class ="bg-warning"]')

    def compare(self):
        percentage_str = self.orange.text_content().split(': ')[1]
        #print(percentage_str)
        #print(self.percent_chrome_locator.text_content())
        return percentage_str == self.percent_chrome_locator.text_content()


