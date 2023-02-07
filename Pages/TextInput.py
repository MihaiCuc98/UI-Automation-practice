import time
from playwright.sync_api import expect, Page

class TextInput:
    def __init__(self, page: Page):
        self.page = page
        self.input_field = page.locator('id=newButtonName')
        self.button = page.locator('id=updatingButton')

    def input_text(self, str):
        self.input_field.fill(str)

    def click_new_button(self):
        self.button.click()