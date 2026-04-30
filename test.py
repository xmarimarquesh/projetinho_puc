def sum_numbers(a, b):
    return a + b

def test_soma_simples():
    assert sum_numbers(1, 2) == 3

def test_soma_negativos():
    assert sum_numbers(-1, -1) == -2

def test_soma_com_zero():
    assert sum_numbers(5, 0) == 5

def test_resultado_errado():
    assert sum_numbers(2, 2) != 5

def test_tipo_retorno():
    assert isinstance(sum_numbers(1, 1), int)