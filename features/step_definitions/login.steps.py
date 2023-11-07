from behave import given, when, then, after
from selenium import webdriver
from selenium.webdriver.common.by import By

@given("Que tengo un navegador abierto")
def navegador_abierto(context):
    context.navegador = webdriver.Chrome()
    context.navegador.implicitly_wait(30)

@when("Entro a la página de de mi aplicación: {string}")
def entro_a_pagina(context, url):
    context.navegador.get(url)

@when("Hago click en el botón con id {string}")
def hago_click_en_boton(context, id):
    context.navegador.find_element(By.ID,id).click()

@when("Escribo {string} en el campo con id {string}")
def escribo_en_campo(context, texto, id):
    elemento = context.navegador.find_element_by_id(By.ID,id)
    elemento.clear()
    elemento.send_keys(texto)

@then("Debería encontrar un elemento con XPATH {string} con texto {string}")
def comprobar_subtitulo(context, xpath, texto):
    elemento=context.navegador.find_element(By.XPATH(xpath))
    assert elemento.text == texto

@then("Debería encontrar un elemento con XPATH {string}")
def comprobar_subtitulo(context, xpath, texto):
    elemento=context.navegador.find_element(By.XPATH(xpath))
    assert elemento is not None

@given("Que he hecho login en la aplicación correctamente")
def login_ok(context):
    context.navegador.get("https://katalon-demo-cura.herokuapp.com/")
    context.navegador.find_element(By.ID,"btn-make-appointment").click()
    context.navegador.find_element(By.ID,"txt-username").clear()
    context.navegador.find_element(By.ID,"txt-username").send_keys("John Doe")
    context.navegador.find_element(By.ID,"txt-password").clear()
    context.navegador.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    context.navegador.find_element(By.ID,"btn-login").click()

@after
def cerrar_navegador(context):
    context.navegador.quit()
