from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


def capturar(navegador,carpeta, nombre_captura):
    # Voy a tomar la ruta del nombre del archivo de captura
    import os
    # Creo esa carpeta dentro de la carpeta "capturas"
    crear_carpeta(os.path.join("capturas", carpeta))
    navegador.get_screenshot_as_file(os.path.join("capturas", carpeta, nombre_captura))

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

# context.scenario.name
