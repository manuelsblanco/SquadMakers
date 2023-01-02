from behave import *
from logout import *

use_step_matcher("re")


@given("estoy viendo la página de detalles de un elemento")
def step_impl(context):
    pagina_elementos(context)


@when('hago clic en el botón "Añadir al carrito"')
def step_impl(context):
    button_add = context.driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]')
    button_add.click()
    button_add2 = context.driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    button_add2.click()


@step('hago clic en el enlace "Ver carrito" en la barra de navegación')
def step_impl(context):
    button_cart = context.driver.find_element('xpath', '//*[@id="shopping_cart_container"]/a')
    button_cart.click()


@step('hago clic en el botón "Proceder al pago" en la página del carrito')
def step_impl(context):
    button_checkout = context.driver.find_element('xpath', '//*[@id="checkout"]')
    button_checkout.click()


@then("se abre la página de pago con el elemento añadido al carrito")
def step_impl(context):
    first_name = context.driver.find_element('xpath', '//*[@id="first-name"]')
    last_name = context.driver.find_element('xpath', '//*[@id="last-name"]')
    postal_code = context.driver.find_element('xpath', '//*[@id="postal-code"]')
    first_name.send_keys("Manuel")
    last_name.send_keys("Blanco")
    postal_code.send_keys("11002")
    button_continue = context.driver.find_element('xpath', '//*[@id="continue"]')
    button_continue.click()


@step("puedo introducir mis detalles de pago y confirmar la compra")
def step_impl(context):
    button_finish = context.driver.find_element('xpath', '//*[@id="finish"]')
    button_finish.click()