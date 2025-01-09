from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET),\
            "Basket is not empty"
        
    def should_be_empty_basket_info(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_INFO),\
            "Empty basket info is not presented"
