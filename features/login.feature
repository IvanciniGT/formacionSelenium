#language:es
@login
Característica: Pantalla de login de mi sistema

    Antecedentes:
        Dado        Que tengo un navegador abierto
        #Dado        Que tengo un navegador abierto en modo headless
        Cuando      Entro a la página de mi aplicación: "https://katalon-demo-cura.herokuapp.com"
        Y           Hago click en el botón con id "btn-make-appointment"

    @loginok
    Escenario:  Hacer login con datos correctos
        Cuando      Escribo "John Doe" en el campo con id "txt-username"
        Y           Escribo "ThisIsNotAPassword" en el campo con id "txt-password"
        Y           capturo la pantalla y la nombro "antes_del_login.png"
        Y           Hago click en el botón con id "btn-login"
        Entonces    Debería encontrar un elemento con XPATH "//section[@id="appointment"]//h2"
        Y           capturo la pantalla y la nombro "despues_del_login.png"
        Y           el elemento debería contener tener el texto "Make Appointment"
        Y           remarcar elemento localizado
        Y           sacar foto del elemento localizado llamada "titulo"

    Escenario:  Hacer login sin nombre
        Cuando      Escribo "ThisIsNotAPassword" en el campo con id "txt-password"
        Y           Hago click en el botón con id "btn-login"
        Entonces    Debería encontrar un elemento con XPATH "//section[@id="login"]//*[contains(text(),"Login failed!")] | //*[contains(@class,"text-danger")]"

    Escenario:  Hacer login sin password
        Cuando      Escribo "John Doe" en el campo con id "txt-username"
        Y           Hago click en el botón con id "btn-login"
        Entonces    Debería encontrar un elemento con XPATH "//section[@id="login"]//*[contains(text(),"Login failed!")] | //*[contains(@class,"text-danger")]"

    Escenario:  Hacer login sin password ni nombre
        Cuando      Hago click en el botón con id "btn-login"
        Entonces    Debería encontrar un elemento con XPATH "//section[@id="login"]//*[contains(text(),"Login failed!")] | //*[contains(@class,"text-danger")]"

    Escenario:  Logout
        Dado        Que he hecho login en la aplicación correctamente
