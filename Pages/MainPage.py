from playwright.sync_api import expect, Page


class MainPage:
    URL = 'http://uitestingplayground.com/'
    def __init__(self, page: Page):
        self.page = page
        self.click_page_link = page.locator('xpath=//a[contains(text(),"Click")]')
        self.click_double_click_page = page.locator('xpath=//a[contains(text(),"Hidden Layers")]')
        self.text_input = page.locator('xpath=//a[contains(text(),"Text Input")]')
        self.progress_bar = page.locator('xpath=//a[contains(text(),"Progress Bar")]')
        self.dynamic_table_locator = page.locator('xpath=//a[contains(text(),"Dynamic Table")]')
        self.sample_app_locator = page.locator('xpath=//a[contains(text(),"Sample App")]')
        self.nbsp_locator = page.locator('xpath=//a[contains(text(),"Non-Breaking Space")]')
        self.ajax_locator = page.locator('xpath=//a[contains(text(),"AJAX Data")]')
        self.overlapped = page.locator('xpath=//a[contains(text(),"Overlapped Element")]')
        self.visibility = page.locator('xpath=//a[contains(text(),"Visibility")]')
        self.verify_text = page.locator('xpath=//a[contains(text(),"Verify Text")]')
        self.dynamic_id = page.locator('xpath=//a[contains(text(),"Dynamic ID")]')

    def load(self):
        self.page.goto(self.URL)

    def click_click(self):
        self.click_page_link.click()

    def click_double_click(self):
        self.click_double_click_page.click()
        expect(self.click_double_click_page).to_be_hidden()

    def click_input_text(self):
        self.text_input.click()

    def click_progress_bar(self):
        self.progress_bar.click()

    def click_dynamic_table(self):
        self.dynamic_table_locator.click()

    def click_sample_app(self):
        self.sample_app_locator.click()

    def click_nbsp(self):
        self.nbsp_locator.click()

    def click_ajax(self):
        self.ajax_locator.click()

    def click_overlapped_page(self):
        self.overlapped.click()

    def click_visibility(self):
        self.visibility.click()

    def click_verify_text(self):
        self.verify_text.click()

    def click_dynamic_id(self):
        self.dynamic_id.click()
