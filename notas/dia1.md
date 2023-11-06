
# Selenium?

Es una organización que fabrica 3 herramientas diferentes:

## Selenium Webdriver

Herramienta para automatizar tareas dentro de un navegador web.
Selenium NO SIRVE PARA HACER PRUEBAS.
Para que usamos habitualmente Selenium? Para hacer pruebas.
Vamos a usar selenium en combinación con otro tipo de herramientas y frameworks para hacer pruebas.
En nuestro caso vamos a utilizar PYTHON: UNITTEST (JUNIT, MSTEST, etc) + SELENIUM

Con esta combinación vamos a conseguir automatizar pruebas dentro de un navegador web sobre el frontal de un aplicativo.

Con SELENIUM WEBDRIVER haré pruebas dinámicas + funcionales + de sistema | de aceptación
Con Selenium no puedo hacer pruebas unitarias ni de integración... OJO... que estas pruebas también se hacen en interfaces web:
    - Cypress
    - Karka
    - Webdriver.io

Al trabajar con SELENIUM hemos dicho que vamos a AUTOMATIZAR una prueba.
Qué significa eso? Qué vamos a montar un programa para que pruebe otro programa!

Hemos convertido a los tester en programadores... que no en desarrolladores de software.
Lo que vamos a estar construyendo son scripts... que por cierto, son un tipo de software muy sencillo de construir.
Y vamos a elegir un lenguaje de programación que nos venga guay para montar scripts: PYTHON

Qué necesitamos conocer para poder hacer este tipo de programas de prueba:
- PYTHON
- Selenium Webdriver
- HTML
- CSS
- XPATH

### Hay muchos tipos de software:

Sistema operativo
Driver
Librería
Aplicación
Demonio:
    Servicio
Script **       Un programa que ejecuta una secuencia de tareas... hasta que acaba
Comando

### Qué significa AUTOMATIZAR?

Diseñar una máquina (o un software que cambie el comportamiento de una máquina) para que ejecute unas tareas que antes hacía un ser humano manualmente.
LAVADORA: Antes se lavaba a mano, ahora se lava automáticamente

## Selenium IDE

Esto es una RUINA GIGANTE !!!!
Es una herramienta que nos permite grabar acciones/pruebas dentro de un navegador web y reproducirlas posteriormente = RUINA !!!!
No se usa para nada en el mundo real.

## Selenium Grid

Nos permite montar una granja de servidores donde ejecutar pruebas en paralelo utilizando diferentes navegadores y diferentes versiones de los mismos, incluso diferentes sistemas operativos y dispositivos móviles.

---

# Pruebas de software

## Vocabulario en el mundo del testing

- ERROR     Los humanos somos los que cometemos errores (por estar cansados, por no saber, por no tener tiempo, por no tener ganas, etc)
- DEFECTO   Al cometer un error introducimos un defecto en el sistema/producto
- FALLO     Ese defecto se puede manisfestar en forma de fallo (el sistema/producto no funciona como debería)

## Para qué sirven las pruebas

- Para asegurar el cumplimiento de unos requisitos
- Para encontrar la mayor cantidad posible de FALLOS en un sistema antes de su puesta en producción
  - Una vez identificados los fallos, se procede a subsanar el DEFECTO del producto que lo provoca
  - Para subsanar el DEFECTO debe primero identificarse ese DEFECTO: DEPURACION / DEBUGGING ~> Desarrollo
- Recopilar la mayor cantidad posible de información sobre el FALLO, que permita la rápida identificación del DEFECTO que lo provoca
- Para encontrar la mayor cantidad posible de DEFECTOS en un sistema antes de su puesta en producción
- Haciendo un análisis de causas raíces para identificar los ERRORES Que han dado lugar a los DEFECTOS.. y tomar acciones preventivas para evitar que vuelvan a ocurrir en el futuro. ERRORES -> DEFECTOS -> FALLOS en el futuro
- Conocer más acerca de mi producto
- Mejorar el desarrollo
- Para saber qué tal va mi proyecto. INDICADOR DE PROGRESO
- Para guiar el desarrollo: TEST-FIRST / TDD / BDD / ATDD
    - TEST-FIRST: Escribir las pruebas antes de escribir el código
    - TDD: Test Driven Development: TEST_FIRST + refactorización* en cada iteración
            * refactorización: Técnica de ingeniería de software que tiene como objetivo mejorar la estructura interna de un código fuente sin alterar su comportamiento externo, es decir, sin cambiar su funcionalidad, con el objetivo de mejorar su legibilidad, entendimiento, reducir su complejidad, facilitar su mantenimiento y reducir los tiempos de desarrollo.
            Se comienza por definir pruebas unitarias 
    - BDD y ATDD son evoluciones complementarias de TDD
        BDD se comienza por definir pruebas de Sistema
        ATDD se comienza por definir pruebas de Aceptación 

## Definición de pruebas

A la hora de definir cada prueba, tendremos que definir 3 cosas diferentes:
- CONTEXTO en el que realizamos la prueba                                   Given   Dado un contexto
- ACCION que quiero probar                                                  When    Cuando ejecuto una acción
- LAS PRUEBAS que garanticen que la acción se ejecuta correctamente         Then    Entonces debo tener un resultado esperado

OJO: Las pruebas no se definen al tun tun....
A la hora de definir una prueba , tenemos en cuenta los principio FIRST de desarrollo de pruebas de software

F - Fast                Se debe poder ejecutar en un tiempo razonable
I - Independent         No debe depender de otras pruebas
R - Repeatable          Debe poder repetirse tantas veces como sea necesario y quiera
S - Self-validating     Debe poder determinar por si misma si se cumplen todas las condiciones necesarias para que la prueba sea correcta
T - Timely              Oportuna, en el momento adecuado

## Tipos de pruebas

Las pruebas se clasifican en base a diferentes criterios: PARALELOS ENTRE SI.
Cualquier prueba se debe centrar en una única característica de mi producto/sistema/componente.

### En base al objeto de pruebas

- Pruebas funcionales
- Pruebas no funcionales
  - Pruebas de rendimiento
  - Pruebas de carga
  - Pruebas de estrés
  - Pruebas de seguridad
  - Pruebas de UX
  - Pruebas de HA

### En base al nivel de la prueba (SCOPE)

- unitarias         Se centra en una característica de un componente AISLADO del sistema

        TREN: Motor, asientos, ventanas, puertas, ruedas, sistema de frenado

            Motor: Le meto corriente y a ver si gira
            Asiento: Carga, Estrés, UX, Seguridad
            Sistema de frenado... le meto corriente y a ver si cierran las pinzas.

- integración       Se centra en la COMUNICACION de 2 componentes

            Sistema de frenado + ruedas
            ^                       ^
            Le meto corriente       Que la rueda se pare

- sistema           Se centran en el COMPORTAMIENTO del sistema en su conjunto
            Ya tengo el tren montao... Le doy al PLAY... y va pa'trás
- aceptación        Usualmente son un subconjunto de las anteriores

Si mis pruebas de Sistema pasan todas, necesito hacer pruebas de integración o unitarias? NO
Si ya tengo el tren y funciona... para que cojones necesito hacer una prueba del motor aislado?

Entonces por qué no hacemos directamente las pruebas de sistema y pasamos de las de integración y las unitarias? 
- El truco está en 2 cosas en esa frase que he escrito:
  - Y si no pasan? dónde está el problema? BUSCA !
  - Cuándo puedo hacer las pruebas de sistema? Cuando tengo el sistema... cuando he acabao... y hasta entonces no hago pruebas? Pues bien voy

### En base al procedimiento de ejecución

- estáticas     No requieren poner el sistema en funcionamiento     >   Identificar DEFECTOS
- dinámicas     Requieren poner el sistema en funcionamiento        >   Identificar FALLOS

# Met. ágiles de desarrollo de software

Es una forma de gestionar un proyecto de software... que reemplaza a las formas más tradicionales que veníamos usando hasta ahora (cascada, v, espiral, etc)

La característica principal de los met. ágiles y la mayor diferencia con respecto a usar met. tradicionales es que los met. ágiles el producto se entrega de forma incremental al cliente, en lugar de entregarlo todo de golpe al final del proyecto.
La finalidad de este cambio de mentalidad es conseguir un rápido feedback del cliente, para poder ir adaptando el producto a sus necesidades reales, en lugar de a las que se pensaba que tenía al principio del proyecto.

SPRINT 1: Dia 30 de comenzar un proyecto hago instalación en producción... Una instalación 100% funcional
 Cuidado.. quizás solo con un 5% de la funcionalidad
    Pruebas: 5%
SPRINT 2: Dia 45 segunda entrega +5% de la funcionalidad
    Pruebas 5% antiguo + 5% nuevo = 10%
SPRINT 3: Dia 60 tercera entrega +15% de la funcionalidad
    Pruebas 10% antiguo + 15% nuevo = 25%
SPRINT 4: Dia 75 cuarta entrega +10% de la funcionalidad
    Pruebas 25% antiguo + 10% nuevo = 35%

Y poco a poco le voy dando el producto... y esto le permite a mi cliente ir dando feedback sobre el producto y yo voy adaptando el producto a sus necesidades reales.

Las met ágiles nos han resuelto un problema que teníamos con los met. tradicionales
PERO nos han traído nuevos problemas que antes no teníamos

Cuántas veces hacíamos antes pruebas de un software?    1 al acabar (si acaso)
Y ahora, con las met. ágiles, cuántas veces hacemos pruebas de un software?  En cada entrega

De dónde sale la pasta? y el tiempo? y los recursos para tanta prueba? NO LA HAY
Solo hay 2 soluciones a este dilema:
- SOLUCIÓN 1: No hago pruebas. EVIDENTEMENTE ESTO NO ES UNA SOLUCIÓN
- SOLUCIÓN 2: Automatizar las pruebas!! NO HAY MAS REMEDIO !!!!

> El software funcionando es la MEDIDA principal de progreso.

La MEDIDA principal (la que hay que usar) de progreso(es decir, de cómo va el proyecto) es "el software funcionando". -> INDICADOR DE PROGRESO

El indicador que debo usar para saber qué tal va mi proyecto es el concepto: SOFTWARE FUNCIONANDO.

"SOFTWARE FUNCIONANDO": Un software que funciona.
Y quién dice que un software funciona? LAS PRUEBAS 

---

# Selenium WebDriver

Está basado en un estándar del W3C llamado WebDriver.

W3C? World Wide Web Consortium: 
    - HTML
    - CSS
    - XML
    - XPATH
    - WebDriver

Ese estándar define cómo podemos construir programas que controlen acciones dentro de un navegador web.

Nosotros vamos a crear con Selenium Webdriver un programa que controle un navegador web? NO

Script PYTHON -> Selenium Webdriver -> Un Webdriver -> Navegador web
  ^
  Yo trabajo a este nivel

El Webdriver es un programa que de acuerdo al estándar Webdriver del W3C es capaz de controlar un navegador.
Cada navegador tiene su propio Webdriver.... es más, cada versión de cada navegador tiene su propia versión de su propio Webdriver.

| Navegador | Webdriver     |
| Chrome    | ChromeDriver  |
| Firefox   | GeckoDriver   |
| Edge      | EdgeDriver    |
| Safari    | SafariDriver  |

Si uso la versión de chrome 87.0.4280.88 necesito el ChromeDriver 87.0.4280.88

Para poder ejecutar mis pruebas necesito:
- Python
- Selenium Webdriver (una librería disponible para python... y para otros tantos lenguajes de programación) que permite invocar a un Webdriver
- Un Webdriver (ChromeDriver, GeckoDriver, EdgeDriver, SafariDriver, etc)
- Un navegador web (Chrome, Firefox, Edge, Safari, etc)

La configuración de esas herramientas es un latazo... más que la configuración de las herramientas, lo que es un latazo es mantenerlas actualizadas. ES LO QUE HAY !

Todos los scripts que vamos a montar en PYTHON para hacer pruebas con SELENIUM WEBDRIVER van a tener la misma estructura:
- TAREA 1: Configurar el webdriver
- TAREA 2: Arrancar desde el webdriver el navegador
- TAREA 3: Automatizar tareas dentro del navegador  <<<<< SELENIUM WEBDRIVER
- TAREA 4: Ejecutar unas pruebas > ENTONCES         <<<<< NEcesitamos un framework de pruebas: UNITTEST
- TAREA 5: Cerrar el navegador



# Ejemplo práctico

Probar el formulario de Login de https://katalon-demo-cura.herokuapp.com/

PRUEBA 1: Intentar acceder con usuario y contraseña incorrectos

Pruebas de caja negra: No conozco el código fuente del sistema
    PRUEBA 1.1: Intentar acceder con usuario incorrecto y contraseña correcta
    PRUEBA 1.2: Intentar acceder con usuario correcto y contraseña incorrecta
    Prueba 1.3: Intentar acceder con usuario incorrecto y contraseña incorrecta
    Prueba 1.4: Intentar acceder sin usuario y sin contraseña
    Prueba 1.5: Intentar acceder con usuario correcto y sin contraseña
    Prueba 1.6: Intentar acceder sin usuario y con contraseña correcta
    Prueba 1.7: Intentar acceder con usuario correcto y contraseña en mayúsculas
Pruebas de caja blanca: Conozco el código fuente del sistema
    El desarrollador sabiendo cómo ha implementado el código puede pensar que da igual que un dato esté en blanco o en mayúsculas... que si no cuela no cuela.

PRUEBA 2: Acceder con usuario y contraseña correctos
    Dado:       Tener un usuario y una contraseña registradas en un sistema
    Y:          Tener un navegador con mi app abierta
    Y:          Haber pulsado en el botón de reservar cita                          ***
    Cuando:     Introducimos en el campo usuario el usuario registrado              *** A la hora de identificar esos elementos en mi web
    E:          Introducimos en el campo contraseña la contraseña registrada        *** PROBLEMON ENORME...
    Y:          Pulsamos el botón de login                                          ***     NO HOY... pero en el futuro...
    Entonces:   Debo llegar al formulario de reserva de citas.                              El mnto de ese código es una tortura en Selenium
                                                                                            Aquí es donde vamos a echar mano de XPATH

[PRUEBA 3: SEGURIDAD: Intentar hacer una inyección de código SQL en el campo usuario o de la contraseña]

Pregunta...
Estoy haciendo la página web de un banco | supermercado | ministerio | compañía de venta online | etc

Cuando haga la prueba... sobre qué navegador la quiero hacer? Chrome | Firefox | Edge | Safari | Opera  
    SOBRE TODOS !!!!
Sobre qué versiones de esos navegadores? La última, la antepenúltima, la penúltima? 
    SOBRE LAS 5 últimas!
Sobre qué sistema operativo? EN TODOS !
    - Windows
    - MacOS
    - Linux Ubuntu
    - Android
    - iOS
Y en qué versiones de esos SO? La última, la antepenúltima, la penúltima? 
    SOBRE LAS 5 últimas!
Y ejecutando sobre qué tipo de dispositivo? PC, tablet, Movil

Y de donde saco la pasta? Y el tiempo? Y los recursos? NO HAY

Entonces... qué hago? AUTOMATIZAR LAS PRUEBAS !!!!
Y monto un GRID de selenium.... bueno... mejor lo alquilo!

Qué es un grid de selenium?
Es una granja de servidores y dispositivos donde ejecutar pruebas en paralelo utilizando diferentes navegadores y diferentes versiones de los mismos, incluso diferentes sistemas operativos y dispositivos móviles.

En el día a día tiro de 1 o 2 o 3 navegadores.. y a veces me monto un grid de selenium en mi máquina o en un servidorcito de la empresa...
Cuando voy a instalar en producción, tiro una prueba a lo bruto... para asegurarme que no haya problemas.

El problema es que en montar un grid de selenium podemos tardar: unos 30 segundos.. y no me da tiempo ni a ir a por un café.

# Selenium grid me permite montar esas granjas..

A mi... granjitas de juguete para mis pruebas del día a día
O a terceros... granjotas de verdad de la buena... para las pruebas de verdad de la buena

# Selenium IDE

Selenium IDE es una extensión de navegador, disponible para Chrome y Firefox, que nos permite grabar acciones y pruebas dentro de un navegador web y reproducirlas posteriormente. Esto es una mierda gigante!

Si quereis usar algo como esto, en lugar de Selenium IDE mejor el Katalon Recorder...

Que hace lo mismo, pero más guay y con una funcionalidad de flipar!