import unittest
from cuenta import Cuenta

class TestCuenta(unittest.TestCase):

    def setUp(self):
        """
        Se ejecuta antes de cada prueba
        """
        self.cuenta = Cuenta("Fulanito perez mengano", "001")
    
    #----------- Pruebas DEL CONSTRUCTOR -----------

    def test_validar_saldo(self):
        self.assertEqual(self.cuenta.saldo, 0, "El saldo inicial debe ser 0 por defecto")

    def test_validar_saldo(self):
        self.assertEqual(self.cuenta.cliente, "Fulanito perez mengano" ", ""El cliente no se asigno correctamente")
    #----------- Pruebas DEL DEPOSITO -----------
    def test_Depositar_dinero_valido(self):
        result = self.cuenta.deposito(500)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberia ser 500.00")

    def test_depositar_cantidad_negativa(self):
        result = self.cuenta.deposito(-200)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual deberia ser 0")

    #test para validar seposito en 0

    #----------- Pruebas DEL RETIRO -----------

    #1. test para validar retiro con cantidad 0
    #2. test para validar retiro con cantidad negativa
    #3. test para validar cantidad mayor al saldo     
    def test_validar_retiro(self):
        self.cuenta.deposito(500)
        result = self.cuenta.retiro(400)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberia ser 500.00")  

    def test_validar_retiro__negativa(self):
        result = self.cuenta.retiro(-200)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberia ser 500.00")

    def test_validar_retiro_cantidad_mayor_al_saldo(self):
        result = self.cuenta.retiro(300)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberia ser 500.00")
        


