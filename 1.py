from playwright.sync_api import sync_playwright


def test_example_webkit():
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        assert page.inner_text('title') == 'XYZ Bank'
        page.click('.btn.btn-primary.btn-lg')
        page.screenshot(path='screen/example.jpeg')
        browser.close()

def test_example():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148')
        page = context.new_page()
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
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshots5/example.jpeg')
        page.click("#userSelect")
        page.wait_for_timeout(3000)
        page.screenshot(path='screenshots5/example1.jpeg')
        browser.close()