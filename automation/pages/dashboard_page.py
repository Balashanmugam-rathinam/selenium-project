from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class DashboardPage(BasePage):

    LOGOUT_BTN = (By.ID, "logout-btn")

    def logout(self):
        self.click(*self.LOGOUT_BTN)

    def is_loaded(self):
        return "Dashboard" in self.driver.title