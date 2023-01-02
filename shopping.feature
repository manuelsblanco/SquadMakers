Feature: Compra de elementos
  Como usuario de la aplicación de compras en línea
  Quiero poder añadir elementos al carrito de compras y proceder al pago
  Para poder realizar compras en la aplicación

Scenario: Añadir un elemento al carrito de compras y proceder al pago
  Given estoy viendo la página de detalles de un elemento
  When hago clic en el botón "Añadir al carrito"
  And hago clic en el enlace "Ver carrito" en la barra de navegación
  And hago clic en el botón "Proceder al pago" en la página del carrito
  Then se abre la página de pago con el elemento añadido al carrito
  And puedo introducir mis detalles de pago y confirmar la compra
