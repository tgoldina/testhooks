import pytest

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('String argument expected')
    return x.capitalize()

def test_capital_case():
    assert capital_case('error') == 'Error'

def test_raises_exception_on_nonstring():
    with pytest.raises(TypeError):
        capital_case(0)
