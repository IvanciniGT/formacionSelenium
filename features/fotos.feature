#language:es

Característica: Pantalla de login de mi sistema

    Antecedentes:
        Dado        Que tengo un navegador abierto en modo headless

    @fotos
    # para hacer que solo se ejecute este escenario podríamos 
    # llamar a behave con el argumento --tags=@fotos
    # También podeis poner tags a Features/Características
    Escenario: Sacar capturas de mis fotos
        Cuando      Entro a la página de mi aplicación: "https://es.wikipedia.org/wiki/Salamanca"
        Entonces    localizar los elementos con xpath "//img"
        Y           sacar foto de cada elemento localizado
