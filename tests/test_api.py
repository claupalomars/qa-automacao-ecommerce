import pytest
import requests

BASE_URL = "https://dummyjson.com"


@pytest.mark.integration
def test_consultar_produto_por_id():
    response = requests.get(f"{BASE_URL}/products/1", timeout=10)
    assert response.status_code == 200
    product = response.json()
    assert isinstance(product["id"], int)
    assert product["id"] == 1
    assert isinstance(product["title"], str)
    assert product["title"].strip() != ""
    assert isinstance(product["price"], (int, float))
    assert product["price"] >= 0


@pytest.mark.integration
def test_listar_produtos():
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0
    for product in data["products"]:
        assert "id" in product
        assert "title" in product
        assert "price" in product
