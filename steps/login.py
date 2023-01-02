from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

# Navegador
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


@given(u'que estoy en la página de inicio de sesión')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.get("https://saucedemo.com/")


@when(u'ingreso mis credenciales correctas')
def login(context):
    user_name = context.driver.find_element("name", "user-name")
    password = context.driver.find_element("name", "password")
    user_name.send_keys('standard_user')
    password.send_keys('secret_sauce')


@when(u'hago clic en el botón LOGIN')
def click_login(context):
    button_login = context.driver.find_element("name", "login-button")
    button_login.click()


@then(u'debo ser redirigido a products')
def step_impl(context):
    assert context.driver.current_url == 'https://www.saucedemo.com/inventory.html'


@when(u'ingreso mis credenciales incorrectas')
def bad_login(context):
    user_name = context.driver.find_element("name", "user-name")
    password = context.driver.find_element("name", "password")
    user_name.send_keys('standard_user')
    password.send_keys('secret')


@then(u'debo ver un mensaje de error')
def step_impl(context):
    error_message = context.driver.find_element("xpath", "//*[@id='login_button_container']/div/form/div[3]/h3")
    assert error_message.text == 'Epic sadface: Username and password do not match any user in this service'
