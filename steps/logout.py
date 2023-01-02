from behave import *
from login import *
use_step_matcher("re")


@given("que estoy conectado a la aplicación")
def pagina_elementos(context):
    launch_browser(context)
    login(context)
    click_login(context)

@when("hago clic en el botón de logout")
def logout(context):
    button_menu = context.driver.find_element('xpath', '//*[@id="react-burger-menu-btn"]')
    button_menu.click()
    button_logout = context.driver.find_element('xpath', '//*[@id="logout_sidebar_link"]')
    context.driver.implicitly_wait(10)
    button_logout.click()

@then("se elimina mi sesión y se me redirige a la página de inicio de sesión")
def pagina_inicio(context):
    assert context.driver.current_url == "https://www.saucedemo.com/"

