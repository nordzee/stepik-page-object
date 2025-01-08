from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    # метод для открытия страницы аутентификации
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
    
    # метод, проверяющий наличие ссылки
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
