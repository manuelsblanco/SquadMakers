from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

# Navegador
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


@given(u'que estoy en la página de inicio')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


@when(u'ingreso la URL en el navegador')
def goToLoginPage(context):
    context.driver.get("https://saucedemo.com/")


@then(u'debo ver la página cargada correctamente en el navegador')
def step_impl(context):
    assert context.driver.current_url == 'https://www.saucedemo.com/'


@then(u'cierro el navegador')
def step_impl(context):
    context.driver.close()
    assert True
