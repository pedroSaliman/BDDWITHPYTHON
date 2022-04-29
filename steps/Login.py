from behave import then, given, when

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@given(u'the user can launsh the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when(u'the user open the page as "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"')
def step_impl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")


@then(u'the user enter email as "admin@yourstore.com" and password as "admin"')
def step_impl(context):
    context.driver.find_element_by_id("Email").clear()
    context.driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
    context.driver.find_element_by_id("Password").clear()
    context.driver.find_element_by_id("Password").send_keys("admin")




@then(u'the user click to login button')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[text()='Log in']").click()

@then(u'the user verify login success')
def step_impl(context):
    assert     context.driver.find_element_by_xpath("//div[@class='content-header']/child::h1").text == "Dashboard"



@then(u'the user close the browser')
def step_impl(context):
    context.driver.quit()

