Feature: login
  Como usuario quiero poder iniciar sesión en la aplicación
  para acceder a mi cuenta y a las funcionalidades exclusivas para usuarios registrados.

Scenario: Inicio de sesión exitoso
  Given que estoy en la página de inicio de sesión
  When ingreso mis credenciales correctas
  When hago clic en el botón LOGIN
  Then debo ser redirigido a products

Scenario: Inicio de sesión fallido
  Given que estoy en la página de inicio de sesión
  When ingreso mis credenciales incorrectas
  When hago clic en el botón LOGIN
  Then debo ver un mensaje de error
