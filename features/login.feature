#language:es

Característica: Pantalla de login de mi sistema

    Escenario:  Hacer login con datos correctos
        Dado        Que tengo un navegador abierto
        Cuando      Entro a la página de de mi aplicación: "https://katalon-demo-cura.herokuapp.com"
        Y           Hago click en el botón con id "btn-make-appointment"
        Y           Escribo "John Doe" en el campo con id "txt-username"
        Y           Escribo "ThisIsNotAPassword" en el campo con id "txt-password"
        Y           Hago click en el botón con id "btn-login"
        Entonces    Debería encontrar un elemento con XPATH "//section[@id='appointment']//h2" con texto "Make Appointment"

    Escenario:  Hacer login sin nombre
        Dado        Que tengo un navegador abierto
        Cuando      Entro a la página de de mi aplicación: "https://katalon-demo-cura.herokuapp.com"
        Y           Hago click en el botón con id "btn-make-appointment"
        Y           Escribo "ThisIsNotAPassword" en el campo con id "txt-password"
        Y           Hago click en el botón con id "btn-login"
        Entonces    Debería encontrar un elemento con XPATH "//section[@id='login']//*[contains(text(),'Login failed!'')] | //*[contains(@class,'text-danger')]"

    Escenario:  Hacer login sin password
        Dado        Que tengo un navegador abierto
        Cuando      Entro a la página de de mi aplicación: "https://katalon-demo-cura.herokuapp.com"
        Y           Hago click en el botón con id "btn-make-appointment"
        Y           Escribo "John Doe" en el campo con id "txt-username"
        Y           Hago click en el botón con id "btn-login"
        Entonces    Debería encontrar un elemento con XPATH "//section[@id='login']//*[contains(text(),'Login failed!'')] | //*[contains(@class,'text-danger')]"

    Escenario:  Hacer login sin password ni nombre
        Dado        Que tengo un navegador abierto
        Cuando      Entro a la página de de mi aplicación: "https://katalon-demo-cura.herokuapp.com"
        Y           Hago click en el botón con id "btn-make-appointment"
        Y           Hago click en el botón con id "btn-login"
        Entonces    Debería encontrar un elemento con XPATH "//section[@id='login']//*[contains(text(),'Login failed!'')] | //*[contains(@class,'text-danger')]"

    Escenario:  Logout
        Dado       Que tengo un navegador abierto
        Y          Que he hecho login en la aplicación correctamente
