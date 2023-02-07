import time

from playwright.sync_api import Page

class OverlappedElement:
    def __init__(self, page: Page):
        self.page = page
        self.name_field = page.locator('xpath=//input[@id="name"]')
        self.id_field = page.locator('xpath =//input[@id="id"]')

    def complete_field(self, id_id, name):
        self.id_field.fill(id_id)
        self.name_field.fill(name)
        self.page.screenshot(path="Screens/aici.png", full_page= True)
        assert self.name_field.is_visible() == True

