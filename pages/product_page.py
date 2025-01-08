from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # метод проверки структуры страницы продукта
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_book_name()
        self.should_be_book_price()
    
    # наличие кнопки "добавить в корзину"
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket' button is not presented"

    # наличие названия книги
    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name title is not presented"
    
    # наличие цены книги
    def should_be_book_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    # метод добавления продукта в корзину
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    # проверки на успешное добавление продукта
    def product_added_to_busket(self):
        self.should_be_product_added_notification()
        self.product_name_in_product_added_notification()
        self.should_be_basket_value_notification()
        self.basket_value_equals_product_price()

    # наличие сообщения о том, что товар добавлен в корзину
    def should_be_product_added_notification(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_NOTIF), "'Product added to basket' notification is not present"

    # проверка названия товара в сообщении
    def product_name_in_product_added_notification(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_notif = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_NOTIF).text
        assert product_name == product_name_in_notif, "Wrong product name in the notification"

    #наличие сообщения со стоимостью корзины
    def should_be_basket_value_notification(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_VALUE_NOTIF), "Basket value notification is not present"

    # проверка, что стоимость корзины совпадает с ценой товара
    def basket_value_equals_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_notif = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_NOTIF).text
        assert product_price == product_price_in_notif, "Wrong basket value in the notification"
