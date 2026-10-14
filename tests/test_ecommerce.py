from decimal import Decimal

import pytest

from src.ecommerce import Cart, Product


@pytest.fixture
def product():
    return Product(id=1, name="Notebook", price=Decimal("2500.00"), stock=5)


@pytest.fixture
def cart():
    return Cart()


def test_adicionar_produto_ao_carrinho(cart, product):
    cart.add_product(product, 1)
    assert cart.items[1][1] == 1


def test_calcular_subtotal(cart, product):
    cart.add_product(product, 2)
    assert cart.subtotal() == Decimal("5000.00")


def test_aplicar_cupom_valido(cart, product):
    cart.add_product(product, 1)
    assert cart.total("QA10") == Decimal("2250.00")


def test_rejeitar_cupom_invalido(cart, product):
    cart.add_product(product, 1)
    with pytest.raises(ValueError, match="Cupom inválido"):
        cart.total("INVALIDO")


@pytest.mark.parametrize("quantity", [0, -1, 1.5, True])
def test_rejeitar_quantidade_invalida(cart, product, quantity):
    with pytest.raises(ValueError):
        cart.add_product(product, quantity)


def test_rejeitar_quantidade_acima_do_estoque(cart, product):
    with pytest.raises(ValueError, match="Estoque insuficiente"):
        cart.add_product(product, 6)


def test_rejeitar_excesso_ao_adicionar_produto_novamente(cart, product):
    cart.add_product(product, 3)
    with pytest.raises(ValueError, match="Estoque insuficiente"):
        cart.add_product(product, 3)


def test_nao_finalizar_carrinho_vazio(cart):
    with pytest.raises(ValueError, match="carrinho vazio"):
        cart.checkout()


def test_finalizar_compra_com_sucesso(cart, product):
    cart.add_product(product, 1)
    assert cart.checkout() == Decimal("2500.00")


def test_finalizar_compra_com_cupom(cart, product):
    cart.add_product(product, 2)
    assert cart.checkout("QA10") == Decimal("4500.00")
