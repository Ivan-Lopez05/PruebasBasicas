from Calculadora import Calculadora
###Clausula de prueba para la función add de la clase Calculadora
def test_add():
    calculadora = Calculadora()
    assert calculadora.add(2, 3) == 5