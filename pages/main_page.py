from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
# from .login_page import LoginPage

class MainPage(BasePage):
    # метод для открытия страницы аутентификации
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        
        # !!!Оставили инициализацию в теле теста
        # при создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес.
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
    
    # метод, проверяющий наличие ссылки
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
