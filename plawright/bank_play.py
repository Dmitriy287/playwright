from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        page.screenshot(path='screenshot6/example.png')
        browser.close()
def test_example():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        assert page.inner_text('title') == 'XYZ Bank'
        page.click("btn.btn-primary.btn-lg")
        page.screenshot(path='screenshot6/example.png')
        browser.close()

def test_example():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        browser.close()
def test_bank_xyz_login():
    with sync_playwright() as p:
            browser = p.firefox.launch()
            page = browser.new_page()
            page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
            assert page.title() == 'XYZ Bank'
            page.click("button.btn.btn-primary")
            page.screenshot(path='screenshots3/example.jpeg')
            page.click("#userSelect")
            page.wait_for_timeout(3000)
            page.screenshot(path='screenshots3/example1.jpeg')
            browser.close()