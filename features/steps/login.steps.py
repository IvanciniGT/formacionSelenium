from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

# hook de behave. Son funciones que de existir, behave ejecuta automaticamente en distintos momentos
# Ejemplos:
# before_all: Se ejecuta antes de comenzar la ejecución de todas las pruebas
# before_feature: Se ejecuta antes de comenzar la ejecución de cada feature
# before_scenario: Se ejecuta antes de comenzar la ejecución de cada scenario
# before_step: Se ejecuta antes de comenzar la ejecución de cada step
# after_step: Se ejecuta después de terminar la ejecución de cada step
# after_scenario: Se ejecuta después de terminar la ejecución de cada scenario
# after_feature: Se ejecuta después de terminar la ejecución de cada feature
# after_all: Se ejecuta después de terminar la ejecución de todas las pruebas

def before_all(context):
    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                          # and if it doesn't exist, download it automatically,
                                          # then add chromedriver to path

def capturar(navegador,carpeta, nombre_captura):
    # Voy a tomar la ruta del nombre del archivo de captura
    import os
    # Creo esa carpeta dentro de la carpeta "capturas"
    crear_carpeta(os.path.join("capturas", carpeta))
    navegador.get_screenshot_as_file(os.path.join("capturas", carpeta, nombre_captura))

def capturar_elemento(elemento,carpeta, nombre_captura):
    if(elemento.size["height"]==0 or elemento.size["width"]==0):
        return
    # Voy a tomar la ruta del nombre del archivo de captura
    import os
    # Creo esa carpeta dentro de la carpeta "capturas"
    crear_carpeta(os.path.join("capturas", carpeta))
    elemento.screenshot(os.path.join("capturas", carpeta, nombre_captura))

def crear_carpeta(carpeta):
    import os
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

@given('capturo la pantalla y la nombro "{nombre_captura}"')
@when('capturo la pantalla y la nombro "{nombre_captura}"')
@then('capturo la pantalla y la nombro "{nombre_captura}"')
def navegador_abierto(context, nombre_captura):
    capturar(context.navegador,context.scenario.name, nombre_captura)

@given("Que tengo un navegador abierto")
def navegador_abierto(context):
    context.navegador = webdriver.Chrome()
    context.navegador.implicitly_wait(30)

@given("Que tengo un navegador abierto en modo headless")
def navegador_abierto(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    context.navegador = webdriver.Chrome(options=chrome_options)
    context.navegador.implicitly_wait(30)

@when('Entro a la página de mi aplicación: "{url}"')
def entro_a_pagina(context, url):
    context.navegador.get(url)

@when('Hago click en el botón con id "{id}"')
def hago_click_en_boton(context, id):
    context.navegador.find_element(By.ID,id).click()

@when('Escribo "{texto}" en el campo con id "{id}"')
def escribo_en_campo(context, texto, id):
    elemento = context.navegador.find_element(By.ID,id)
    elemento.clear()
    elemento.send_keys(texto)

@then('el elemento debería contener tener el texto "{texto}"')
def comprobar_subtitulo(context,texto):
    assert context.elemento.text == texto

@then('Debería encontrar un elemento con XPATH "{xpath}"')
def comprobar_subtitulo(context, xpath):
    context.elemento=context.navegador.find_element(By.XPATH,xpath)
    assert context.elemento is not None

@given("Que he hecho login en la aplicación correctamente")
def login_ok(context):
    context.navegador.get("https://katalon-demo-cura.herokuapp.com/")
    context.navegador.find_element(By.ID,"btn-make-appointment").click()
    context.navegador.find_element(By.ID,"txt-username").clear()
    context.navegador.find_element(By.ID,"txt-username").send_keys("John Doe")
    context.navegador.find_element(By.ID,"txt-password").clear()
    context.navegador.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    context.navegador.find_element(By.ID,"btn-login").click()

@then('localizar los elementos con xpath "{xpath}"')
def localizar_elementos(context, xpath):
    context.elementos=context.navegador.find_elements(By.XPATH,xpath)

@then('sacar foto de cada elemento localizado')
def localizar_elementos(context):
    numero_elemento = 1
    for elemento in context.elementos:
        capturar_elemento(elemento,context.scenario.name, "elemento_"+str(numero_elemento)+".png")
        numero_elemento += 1
    

def after_scenario(context, scenario):
    context.navegador.quit()