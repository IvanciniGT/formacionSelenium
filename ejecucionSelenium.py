from selenium import webdriver
from selenium.webdriver.common.by import By

# Abrir un navegador chrome 
# Navegador en local 
driver = webdriver.Chrome()
# Navegador en un entorno remoto GRID DE SELENIUM
options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor='http://34.249.57.30:4444/wd/hub',options=options)

# Configurar que si un elemento no se encuentra, se espere hasta 30 segundos antes de dar la ejecución por fallida
# Esto puede deberse a problemas puntuales en la conexión de red.. o que una página tarde mucho en cargar
driver.implicitly_wait(30)

# Vete a una página concreta en el navegador
driver.get("https://katalon-demo-cura.herokuapp.com/")
# Busca un elemento                                                 # Sobre ese elemento ejecuta una acción
driver.find_element(By.ID,"btn-make-appointment")                                  .click()
driver.find_element(By.ID,"txt-username")                                          .clear()
driver.find_element(By.ID,"txt-username")                                          .send_keys("John Doe")
driver.find_element(By.ID,"txt-password")                                          .clear()
driver.find_element(By.ID,"txt-password")                                          .send_keys("ThisIsNotAPassword")
driver.find_element(By.ID,"btn-login")                                             .click()
texto=driver.find_element(By.XPATH,"//section[@id='appointment']//h2")             .text

# Cierra el navegador
driver.quit()

print(texto)
