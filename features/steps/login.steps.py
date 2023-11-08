from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

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
