from playwright.sync_api import sync_playwright, Page, BrowserContext
import pytest
from locator import *
from test_data import *
from playwright.sync_api import expect

@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.firefox.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def login_bank_customer(page: Page):
    def login_function():
        page.goto(driver_get_bankxyz)
        page.click(locator_button_login_customer)
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshot/login.png')
    return login_function


@pytest.fixture
def login_bank_potter(page: Page):
    def login_bank_potter_function():
        page.click(locator_button_your_name)
        page.select_option(locator_button_your_name, label='Harry Potter')
        page.click(locator_button_login)
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshot/log.png')
    return login_bank_potter_function

@pytest.fixture
def bank_home(page: Page):
    def bank_home_function():
        page.click(locator_button_back_home)
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshot/home.png')
    return bank_home_function

@pytest.fixture
def login_bank_weasly(page: Page):  # pytest -k login test_step.py
    def login_bank_weasly_function():
        page.click(locator_button_your_name)
        page.select_option(locator_button_your_name, label='Ron Weasly')
        page.click(locator_button_login)
        page.wait_for_timeout(3000)
    return login_bank_weasly_function

@pytest.fixture
def logout_bank(page: Page):
    def logout_bank_function():
        page.click(locator_button_logout)
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshot/logout.png')
    return logout_bank_function

@pytest.fixture
def deposit(page: Page):
    def deposit_function():
        page.click(locator_button_account_select)
        page.select_option(locator_button_account_select, label='1005')
        page.click(locator_button_deposit)
        page.fill(locator_field_amount, data_deposit)
        page.click(locator_deposit)
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshot/deposit.png')
    return deposit_function

@pytest.fixture
def withdrawl(page: Page):
    def withdrawl_function():
        page.click(locator_button_account_select)
        page.select_option(locator_button_account_select, label='1005')
        page.click(locator_button_withdrawl)
        page.wait_for_timeout(3000)
        page.click(locator_field_amount_withdrawn)
        page.fill(locator_field_amount, data_with_drawl)
        page.wait_for_timeout(3000)
        page.click(locator_button_withdraw)
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshot/wi.png')
    return withdrawl_function

@pytest.fixture
def transaction(page: Page):
    def transaction_function():
        page.click(locator_button_transactions)
        page.wait_for_timeout(2000)
        page.click(locator_scroll_right)
        page.wait_for_timeout(2000)
        page.screenshot(path='screenshot/tran.png')
        page.click(locator_transactions_reset)
        page.wait_for_timeout(2000)
    return transaction_function

@pytest.fixture
def login_bank_manager(page: Page):
    def login_bank_manager_function():
        page.goto(driver_get_bankxyz)
        page.click(locator_button_login_bank_manager)
        page.wait_for_timeout(2000)
    return login_bank_manager_function

@pytest.fixture
def add_customer(page: Page):
    def add_customer_function():
        page.click(locator_button_add_customer)
        page.fill(locator_first_name, data_first_name)
        page.wait_for_timeout(2000)
        page.fill(locator_last_name, data_last_name)
        page.wait_for_timeout(2000)
        page.fill(locator_post_code, data_post_code)
        page.wait_for_timeout(2000)
        page.click(locator_button_add_customer_confirm)
        page.wait_for_timeout(2000)
        page.click(locator_button_list_customer)
        page.wait_for_timeout(2000)
        page.fill(locator_search_customer, data_first_name)
        page.wait_for_timeout(2000)
        page.screenshot(path='screenshot/add.png')
    return add_customer_function


@pytest.fixture
def open_account(page: Page):
    def open_account_function():
        page.click(locator_button_open_account)
        page.click(locator_customer_name)
        page.select_option(locator_customer_name, label='Harry Potter')
        page.wait_for_timeout(3000)
        page.click(locator_currency)
        page.select_option(locator_currency, label='Rupee')
        page.wait_for_timeout(1000)
        page.click(locator_process)
        page.wait_for_timeout(2000)
        page.screenshot(path='screenshot/open.png')
    return open_account_function

@pytest.fixture
def list_customer(page: Page):
    def list_customer_function():
        page.click(locator_button_list_customer)
        page.wait_for_timeout(2000)
        page.screenshot(path='screenshot/list.png')
    return list_customer_function

