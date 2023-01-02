Feature: Abrir Login Page


Scenario: Abrir Login Page exitoso
  Given que estoy en la página de inicio
  When ingreso la URL en el navegador
  Then debo ver la página cargada correctamente en el navegador
  Then cierro el navegador
