from Calculadora import Calculadora

def test_add():
    calculadora = Calculadora()
    assert calculadora.add(2, 3) == 5