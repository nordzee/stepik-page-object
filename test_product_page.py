import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('offer_id', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='under bug fix process')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, offer_id):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_id}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added_to_busket()
