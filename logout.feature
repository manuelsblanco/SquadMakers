Feature: Logout
  Como usuario quiero poder cerrar sesión en la aplicación
  para proteger mi privacidad y seguridad.

Scenario: Cerrar sesión
  Given que estoy conectado a la aplicación
  When hago clic en el botón de logout
  Then se elimina mi sesión y se me redirige a la página de inicio de sesión
