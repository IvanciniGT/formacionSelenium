
# Identificación de elementos en el HTML desde SELENIUM

Selenium busca elementos en el DOM de la página web.

Lo que nunca falla a la hora de identificar elementos es tener un IDENTIFICADOR ÚNICO.

```py
#                        FORMA DE IDENTIFICAR      DATOS_ADICIONALES
#                                       v           v
elemento = navegador.find_element(   By.ID     , "el identificador"  ) 
elemento = navegador.find_element(   By.XPATH  , "el xpath"          ) 
elemento = navegador.find_element(   By.CSS    , "el css"            )
elemento = navegador.find_element(   By.LINK_TEXT, "el link text"    )
```

El problema es siempre voy a encontrar elementos sobre los que los desarrolladores no han puesto identificadores únicos = PROBLEMÓN GORDO!

Acciones a tomar en este momento: 
Opción 1: INTENTAR DENTRO DE MIS POSIBILIDADES QUE EL EQUIPO DE DESARROLLO PONGA IDENTIFICADORES ÚNICOS A LOS ELEMENTOS QUE NECESITO.
          Lo guay es que yo hubiera definido los test, antes que el desarrollador haya hecho el código: TEST-FIRST DEVELOPMENT
          Basado en TEST-FIRST hay otras metodologías: TDD, BDD, ATDD
            Esta sería la mejor forma posible de trabajar, y la tendencia hoy en día en la industria.
            En España... sabéis que vamos con un poco de retraso en esto. Y esto en muchos casos es CIENCIA FICCIÓN.
Opción 2: Leer OPCIÓN 1
Opción 3: Cuando he tirado la toalla de la opción 1 y opción 2
            Voy a ver la mejor estrategia posible para identificar un elemento y que se mantenga a lo largo del tiempo operativo

            Además de trabajar con IDENTIFICADORES ÚNICOS, selenium nos permite trabajar con otros tipos de identificadores:
                - XPATH             <<<< SOLO NECESITAIS APRENDER ESTA
                - CSS SELECTOR
                - LINK TEXT
  
XPATH es una sintaxis definida en un estándar del W3C (del mismo nivel que XML, HTML, CSS) que permite identificar elementos en una estructura jerárquica de nodos, como por ejemplo el DOM de una página web.

Pero con XPATH puedo sacar 500 formas diferentes de identificar un elemento. Experiencia es lo que me hace falta para de esas 500 formas, elegir la que vaya a tener más garantías de seguir operativa en el futuro.

## Sintaxis XPATH

Lo que buscamos es identificar nodo"S" dentro de un DOM de una página web.

### Caracteres especiales en la sintaxis de XPATH

- //  :  Buscar un elemento dentro de donde estoy hacia abajo en cualquier nivel del DOM
- /   :  Buscar un elemento dentro de donde estoy del DOM
         Si empieza al principio del XPATH, significa elemento RAIZ del DOM
- *   :  Buscar cualquier elemento
- .   :  Donde estoy
- tipo: Elemento de un determinado tipo

HTML                        1
  HEAD                      2
    TITLE                   3
    LINK                    4
  BODY                      5
    DIV                     6
      H1                    7
      P                     8
      DIV                   9
        P                   10
    DIV                     11
        P                   12
        P                   13
        H2                  14
        P                   15
        DIV                 16
            P               17
        OL                  18
            LI              19
                P           20
/HTML/BODY/DIV/H1               7
/HTML/BODY//H1                  7
/HTML//DIV/H1                   7
//H1                            7
//DIV/H1                        7
//BODY//H1                      7
//DIV/P                         8, 10, 12, 13, 15, 17
//DIV/DIV/P                     10, 17
//DIV/*/P                       10, 17
//DIV//*/P                      10, 17, 20


HTML                        1
  HEAD                      2
    TITLE                   3
    LINK                    4
  BODY                      5
    DIV id="div1"           6
      H1                    7
      P                     8
      DIV                   9
        P                   10
    DIV                     11
        P                   12
        P                   13
        H2 class="titulo"   14
        P                   15
        DIV                 16
            P               17
        OL                  18
            LI              19
                P           20
                P           21
        H2                  22

//H2[@class="titulo"]       14
//DIV[@id="div1"]           6
//*[@id="div1"]             6

Cuando vemos corchetes en XPATH los leemos: "TAL QUE"
//*[@id="div1"]//P          8, 10
//DIV[./H1]//P              8, 10
Búsqueme un elemento DIV, tal que tenga dentro un elemento H1... y de ese DIV me traiga todos los elementos P que tenga dentro a cualquier nivel
//DIV//P[position() = 1]    8, 10, 12, 17, 20
La búsqueda por position se hace en cada nivel
//DIV//P[position() = last()]  8, 10, 15, 17, 21
    
#    text() EXTRAE EL TEXTO DE UN ELEMENTO

//H1/text()                "Título de la página"
//DIV/P[text() = "Texto del párrafo"]
//DIV/P[contains(text(), "Texto del párrafo")]
//DIV[.//H1[contains(text(), "Título")]]//P[1]

//*[@id="btn-make-appointment"]
/html/body/header/div/a

//h1[contains(text(),'CURA Healthcare Service')]