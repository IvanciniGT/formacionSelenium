import unittest

class MiClaseDePruebas(unittest.TestCase):

    def setUp(self):
        print("Esta función se ejecuta cuando van a comenzar las pruebas")

    def test_federico(self):
        """Esta es la prueba de la suma"""
        print("Aqui pondríamos el código de una prueba")
        # De lo que parto
        numero1 = 5
        numero2 = 7
        # Accion que quiero probar que se ejecuta adecuandamente
        resultado = numero1 + numero2
        # Comprobación
        self.assertEqual(resultado, 12) # <<<<<<   ESTA ES LA PRUEBA

    def test_menchu(self):
        print("Aqui pondríamos el código de otra prueba")
        
    def tearDown(self):
        print("Esta función se ejecuta al finalizar las pruebas")

if __name__ == "__main__":
    unittest.main() # Esto es lo que lanza la ejecución de las pruebas
                    # Esa función va a crear una instancia de nuestra clase automáticamente y a ejecutar:
                    # Primero: setUp
                    # Segundo: federico y menchu.. en cualquier orden... No se respeta el orden de escritura
                    # Tercero: tearDown
