import unittest
from calculadora import sumar  # Importamos la función a probar

class TestCalculadora(unittest.TestCase):

    def test_sumar_numeros_positivos(self):
        self.assertEqual(sumar(3, 5), 8)  # 3 + 5 debe ser 8

    def test_sumar_numeros_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)  # -2 + -3 debe ser -5

    def test_sumar_cero(self):
        self.assertEqual(sumar(0, 5), 5)  # 0 + 5 debe ser 5

# Esto permite ejecutar las pruebas al correr el archivo
if __name__ == '__main__':
    unittest.main()

#Dany Alexander Ramirez Rivas
#danyr7196@gmail.com