from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators

class BasePage():
    # добавляем конструктор-метод
    # внутри конструктора сохраняем экземпляр драйвера и url адрес как аттрибуты нашего класса
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)
    
    # метод для открывания страницы в браузере
    def open(self):
        self.browser.get(self.url)

    # вспомогательный метод поиска элемента с обработкой ошибки 
    def is_element_present(self, selector_type, selector_value):
        try:
            self.browser.find_element(selector_type, selector_value)
        except NoSuchElementException:
            return False
        return True

    # вспомогательный метод проверки отсутствия элемента (когда что-то может появиться, а не должно)
    def is_not_element_present(self, selector_type, selector_value, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((selector_type, selector_value)))
        except TimeoutException:
            return True
        return False

    # вспомогательный метод проверки исчезающих компонентов 
    def is_disappeared(self, selector_type, selector_value, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((selector_type, selector_value)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not presented"

    # метод для получения кода проверки заданий в stepik
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
