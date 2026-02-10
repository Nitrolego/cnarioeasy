import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_empty_fields(playwright: Playwright):
    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/login-flow#challenge")

    #test: click the login button with empty fields
    page.get_by_role("button", name="Login").click()

    #assert: error message is visible
    expect(page.get_by_text("Both fields are required.")).to_be_visible()
    
    #clean up
    context.close()
    browser.close()

def test_invalid_credentials(playwright: Playwright):
    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/login-flow#challenge")

    #test: click the login button with invalid credentials
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("wrongUser")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("wrongPass")
    page.get_by_role("button", name="Login").click()

    #assert: error message is visible
    expect(page.get_by_text("Invalid username or password.")).to_be_visible()
    
    #clean up
    context.close()
    browser.close()

def test_login_as_user(playwright: Playwright):
    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/login-flow#challenge")

    #test: click the login button with user credentials
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("user123")
    page.get_by_role("button", name="Login").click()

    #assert: error message is visible
    expect(page.get_by_text("You are logged in as USER")).to_be_visible()
    
    #clean up
    context.close()
    browser.close()

def test_login_as_admin(playwright: Playwright):
    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/login-flow#challenge")

    #test: click the login button with admin credentials
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    #assert: error message is visible
    expect(page.get_by_text("You are logged in as ADMIN")).to_be_visible()
    
    #clean up
    context.close()
    browser.close()

def test_logout_user(playwright: Playwright):
    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/login-flow#challenge")

    #setup: login as user
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("user")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("user123")
    page.get_by_role("button", name="Login").click()

    #test: click the logout button
    page.get_by_role("button", name="Logout").click()

    #assert: logout successful (see login form)
    expect(page.get_by_role("heading", name="Login", exact=True)).to_be_visible()
    expect(page.get_by_role("textbox", name="Username")).to_be_empty()
    expect(page.get_by_role("textbox", name="Password")).to_be_empty()
    
    #clean up
    context.close()
    browser.close()

def test_logout_admin(playwright: Playwright):
    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/login-flow#challenge")

    #setup: login as admin
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    #test: click the logout button
    page.get_by_role("button", name="Logout").click()

    #assert: logout successful (see login form)
    expect(page.get_by_role("heading", name="Login", exact=True)).to_be_visible()
    expect(page.get_by_role("textbox", name="Username")).to_be_empty()
    expect(page.get_by_role("textbox", name="Password")).to_be_empty()
    
    #clean up
    context.close()
    browser.close()