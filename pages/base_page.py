class BasePage():
    # добавляем конструктор-метод
    # внутри конструктора сохраняем экземпляр драйвера и url адрес как аттрибуты нашего класса
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    # метод для открывания страницы в браузере
    def open(self):
        self.browser.get(self.url)
