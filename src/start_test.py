from .start import soma


def test_soma():
    """testing soma"""

    resultado = soma(2, 4)
    assert resultado == 6
