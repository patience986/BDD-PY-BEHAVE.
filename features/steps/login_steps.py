from behave import given, when, then
from selenium import webdriver

@given("the user is on the login page")
def step_open_login_page(context):
    context.browser = webdriver.Chrome()  # Or any WebDriver setup
    context.browser.get("http://example.com/login")

@when("the user enters valid credentials")
def step_enter_valid_credentials(context):
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("correctpassword")
    context.browser.find_element_by_name("login").click()

@when("the user enters invalid credentials")
def step_enter_invalid_credentials(context):
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("wrongpassword")
    context.browser.find_element_by_name("login").click()

@then("the user is redirected to the dashboard")
def step_redirected_to_dashboard(context):
    assert "dashboard" in context.browser.current_url
    context.browser.quit()

@then("an error message is displayed")
def step_error_message_displayed(context):
    error_message = context.browser.find_element_by_id("error").text
    assert error_message == "Invalid credentials"
    context.browser.quit()
