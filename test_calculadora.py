from Calculadora import Calculadora
###Clausula de prueba para la función add de la clase Calculadora
def test_add():
    calculadora = Calculadora()
    assert calculadora.add(2, 3) == 5
###Clausula de prueba para la función subtract de la clase Calculadora
def test_subtract():
    calculadora = Calculadora()
    assert calculadora.subtract(5, 2) == 3