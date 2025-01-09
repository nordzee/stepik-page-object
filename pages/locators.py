from selenium.webdriver.common.by import By

# локаторы главной страницы
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# локаторы страницы логина
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

# локаторы страницы продукта
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_ADDED_NOTIF = (By.CSS_SELECTOR, ".alert:first-of-type  strong")
    BASKET_VALUE_NOTIF = (By.CSS_SELECTOR, ".alert:last-of-type strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
