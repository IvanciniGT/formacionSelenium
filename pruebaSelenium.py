import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MiClaseDePruebas(unittest.TestCase):

    def setUp(self):
        # Abrir un navegador chrome 
        self.navegador = webdriver.Chrome()
        # Configurar que si un elemento no se encuentra, se espere hasta 30 segundos antes de dar la ejecución por fallida
        # Esto puede deberse a problemas puntuales en la conexión de red.. o que una página tarde mucho en cargar
        self.navegador.implicitly_wait(30)

    def test_login_ok(self):
        """Login con datos correctos"""
        # Vete a una página concreta en el navegador
        self.navegador.get("https://katalon-demo-cura.herokuapp.com/")
        # Busca un elemento                                                 # Sobre ese elemento ejecuta una acción
        self.navegador.find_element(By.ID,"btn-make-appointment")                                  .click()
        self.navegador.find_element(By.ID,"txt-username")                                          .clear()
        self.navegador.find_element(By.ID,"txt-username")                                          .send_keys("John Doe")
        self.navegador.find_element(By.ID,"txt-password")                                          .clear()
        self.navegador.find_element(By.ID,"txt-password")                                          .send_keys("ThisIsNotAPassword")
        self.capturar("capturas/login_ok/captura_antes_login_ok.png")
        self.navegador.find_element(By.ID,"btn-login")                                             .click()
        texto=self.navegador.find_element(By.XPATH,"//section[@id='appointment']//h2")             .text
        self.capturar("capturas/login_ok/captura_despues_login_ok.png")
        # COMPROBACION DE QUE EL TEXTO ES EL ESPERADO
        self.assertEqual(texto,"Make Appointment")

    def test_login_nok(self):
        """Login con datos correctos"""
        # Vete a una página concreta en el navegador
        self.navegador.get("https://katalon-demo-cura.herokuapp.com/")
        # Busca un elemento                                                 # Sobre ese elemento ejecuta una acción
        self.navegador.find_element(By.ID,"btn-make-appointment")                                  .click()
        self.navegador.find_element(By.ID,"txt-username")                                          .clear()
        self.navegador.find_element(By.ID,"txt-username")                                          .send_keys("John Doe")
        self.navegador.find_element(By.ID,"txt-password")                                          .clear()
        self.navegador.find_element(By.ID,"txt-password")                                          .send_keys("RUINA")
        self.capturar("capturas/login_nok/captura_antes_login_nok.png")
        self.navegador.find_element(By.ID,"btn-login")                                             .click()
        elemento=self.navegador.find_element(By.XPATH,'//section[@id="login"]//*[contains(text(),"Login failed!")] | //*[contains(@class,"text-danger")]')
        # COMPROBACION DE QUE EL TEXTO ES EL ESPERADO
        self.capturar("capturas/login_nok/captura_despues_login_nok.png")
        self.assertIsNotNone(elemento)

    def tearDown(self):
        # Cierra el navegador
        self.navegador.quit()

    def capturar(self, nombre_captura):
        # Voy a tomar la ruta del nombre del archivo de captura
        import os
        self.crear_carpeta(os.path.dirname(nombre_captura))
        self.navegador.get_screenshot_as_file(nombre_captura)

    def crear_carpeta(self, carpeta):
        import os
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

if __name__ == "__main__":
    unittest.main() # Esto es lo que lanza la ejecución de las pruebas
                    # Esa función va a crear una instancia de nuestra clase automáticamente y a ejecutar:
                    # Primero: setUp
                    # Segundo: federico y menchu.. en cualquier orden... No se respeta el orden de escritura
                    # Tercero: tearDown
