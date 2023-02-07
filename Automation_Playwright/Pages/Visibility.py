from playwright.sync_api import Page


class Visibility:
    def __init__(self, page: Page):
        self.page = page
        self.hidden_button = page.locator('//button[@id="hideButton"]')
        self.removed_button = page.locator('//button[@id="removedButton"]')
        self.zero_width_button = page.locator('//button[@id="zeroWidthButton"]')
        self.overlapped_button = page.locator('//button[@id="overlappedButton"]')
        self.transparent_button = page.locator('//button[@id="transparentButton"]')
        self.visibility_hidden = page.locator('//button[@id="invisibleButton"]')
        self.display_none = page.locator('//button[@id="notdisplayedButton"]')
        self.off_screen = page.locator('//button[@id="offscreenButton"]')


    def hit_hide_button(self):
        self.hidden_button.click()