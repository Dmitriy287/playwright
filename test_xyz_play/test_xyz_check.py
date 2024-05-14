from playwright.sync_api import Page
from test_xyz_step import *

@pytest.mark.smoke_bank
def test_login_bank_customer(page: Page, login_bank_customer):
        """Проверка входа"""
        login_bank_customer()
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/customer" in page.url.lower()
        print('Вход успешный')
        return test_login_bank_customer

@pytest.mark.smoke_bank
def test_login_successful_potter(page: Page, login_bank_customer, login_bank_potter):
    """Проверка входа Гарри Поттер"""
    login_bank_customer()
    login_bank_potter()
    assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/account" in page.url.lower()
    print('Вход Гарри Поттер успешный')
    return test_login_successful_potter
@pytest.mark.smoke_bank
def test_login_and_back_home_successful_potter(page: Page, login_bank_customer, login_bank_potter, bank_home):
        """Проверка входа Гарри Поттер и возврат на главную страницу"""
        login_bank_customer()
        login_bank_potter()
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/account" in page.url.lower()
        print('Вход Гарри Поттер успешный')
        bank_home()
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/login" in page.url.lower()
        print('Переход на главную страницу успешный')
        return test_login_and_back_home_successful_potter
@pytest.mark.smoke_bank
def test_login_successful_weasly(page: Page, login_bank_customer, login_bank_weasly, logout_bank):
        """Проверка входа Рон Уизли и логаут"""
        login_bank_customer()
        login_bank_weasly()
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/account" in page.url.lower()
        print('Вход Рон Уизли успешный')
        logout_bank()
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/customer" in page.url.lower()
        print('Выход успешный')
        return test_login_successful_weasly
@pytest.mark.smoke_bank
def test_successful_deposit_potter(page: Page, login_bank_customer, login_bank_potter, deposit):
        """Проверка депонирования средств"""
        login_bank_customer()
        login_bank_potter()
        deposit()
        assert page.title() == 'XYZ Bank'
        print('Депозит  успешный')
        return test_login_successful_weasly
@pytest.mark.smoke_bank
def test_successful_withdrawl_potter(page: Page, login_bank_customer, login_bank_potter, deposit, withdrawl):
        """Проверка списания средств"""
        login_bank_customer()
        login_bank_potter()
        deposit()
        withdrawl()
        successful_text = page.wait_for_selector(locator_message_successful).text_content()
        assert successful_text == "Transaction successful"
        print('Списание произведено успешно')
        return test_successful_withdrawl_potter

@pytest.mark.smoke_bank
def test_successful_fail_withdrawl_potter(page: Page, login_bank_customer, login_bank_potter, deposit, withdrawl):
        """Проверка списания средств"""
        login_bank_customer()
        login_bank_potter()
        withdrawl()
        successful_text = page.wait_for_selector(locator_message_successful).text_content()
        assert successful_text == "Transaction Failed. You can not withdraw amount more than the balance."
        print('Списание произведено успешно')
        return test_successful_fail_withdrawl_potter

@pytest.mark.smoke_bank
def test_successful_transaction_potter(page: Page, login_bank_customer, login_bank_potter, deposit, withdrawl, transaction):
        """Проверка отчета об операциях"""
        login_bank_customer()
        login_bank_potter()
        deposit()
        withdrawl()
        transaction()
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/listtx" in page.url.lower()
        print('Отчет об операциях сформирован')

@pytest.mark.smoke_bank
def test_login_successful_manager(page: Page, login_bank_manager):
        """Проверка входа работника банка"""
        login_bank_manager()
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/manager" in page.url.lower()
        print('Вход работника успешный')
        return test_login_successful_manager

@pytest.mark.smoke_bank
def test_successful_add_customer(page: Page, login_bank_manager, add_customer, list_customer):
        """Проверка добавления клиента"""
        login_bank_manager()
        add_customer()
        list_customer()
        contains_farell = page.locator(locator_assert_td_ng_binding_1).filter(has_text=data_last_name).count() > 0
        print("Строка не найдена" if not contains_farell else "Строка найдена")
        assert contains_farell, "Строка не найдена"
        print('Клиент добавлен')

@pytest.mark.smoke_bank
def test_successful_open_account_potter(page: Page, login_bank_manager, open_account, add_customer):
                """Проверка открытия счета"""
                login_bank_manager()
                open_account()
                print('Счет открыт успешно')
                return test_successful_open_account_potter

@pytest.mark.smoke_bank
def test_list_customer(page: Page, login_bank_manager, list_customer):
        """Проверка формирования списка клиентов"""
        login_bank_manager()
        list_customer()
        assert "https://www.globalsqa.com/angularjs-protractor/bankingproject/#/manager/list" in page.url.lower()
        print('Список клиентов сформирован успешно')
        return test_list_customer



