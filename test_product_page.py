import pytest
from faker import Faker
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

@pytest.mark.parametrize('offer_id',\
    [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='under bug fix process')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, offer_id):
    offer_link = f"{base_link}/?promo=offer{offer_id}"
    page = ProductPage(browser, offer_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added_to_busket()

@pytest.mark.skip # failed test, тест неактуален 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_product_added_notification()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_not_be_product_added_notification()

@pytest.mark.skip # failed test, тест неактуален 
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_product_added_notification()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_basket_link_on_product_page(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_be_basket_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_empty_basket_info()

class TestUserAddToBasketFromProductPage():
    # setup — функция, которая выполнится перед запуском каждого теста из класса
    # !!!манипулировать браузером в сетапе - плохая практика, надо работать с API. Здесь для примера
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = Faker().email()
        password = Faker().password(length=15)
        link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link_login)
        login_page.open()
        login_page.register_new_user(email, password)


    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, base_link)
        page.open()
        page.add_product_to_basket()
        page.product_added_to_busket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, base_link)
        page.open()
        page.should_not_be_product_added_notification()