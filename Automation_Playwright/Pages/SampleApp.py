from playwright.sync_api import Page


class SampleApp:
    def __init__(self, page: Page):
        self.page = page
        self.user_name = page.locator('xpath=//input[@name="UserName"]')
        self.password = page.locator('xpath=//input[@name="Password"]')
        self.login_button = page.locator('xpath=//button[@id="login"]')
        self.success_login = page.locator('xpath=//label[contains(text(),"Welcome")]')

    def enter_username(self, username):
        self.user_name.fill(username)

    def enter_password(self, ps):
        self.password.fill(ps)

    def click_login(self):
        self.login_button.click()

    def success_logged_in(self) -> bool:
        return self.success_login.is_visible()
