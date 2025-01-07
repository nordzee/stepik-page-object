from selenium.common.exceptions import NoSuchElementException

class BasePage():
    # добавляем конструктор-метод
    # внутри конструктора сохраняем экземпляр драйвера и url адрес как аттрибуты нашего класса
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
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
