from playwright.sync_api import Page
from test_sdp_steps import *

@pytest.mark.smoke_market # pytest -v --headed --slowmo 100 test_sdp_checks.py::test_login_successful
def test_login_successful(page: Page, login, login_successful, logout):
    """Проверка входа"""
    login()
    login_successful()
    logout()

@pytest.mark.smoke_market
def test_logout_successful(page: Page, login, logout, logout_successful):
    """Проверка выхода"""
    login()
    logout()
    logout_successful()

@pytest.mark.smoke_market
def test_sort_products_successful(page: Page, login, logout, sort_products, sort_products_successful):
    """Проверка сортировки"""
    login()
    sort_products()
    sort_products_successful()
    logout()

@pytest.mark.smoke_market
def test_get_product_successful(page: Page, login, logout, get_product, get_product_successful):
    """Проверка покупки"""
    login()
    get_product()
    get_product_successful()
    logout()