from selenium.webdriver.common.by import By

# локаторы главной страницы
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# локаторы страницы логина
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

# локаторы страницы продукта
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_ADDED_NOTIF = (By.CSS_SELECTOR, ".alert:first-of-type  strong")
    BASKET_VALUE_NOTIF = (By.CSS_SELECTOR, ".alert:last-of-type strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_INFO = (By.CSS_SELECTOR, "#content_inner > p")
