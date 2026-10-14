from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


@dataclass
class Product:
    id: int
    name: str
    price: Decimal
    stock: int


@dataclass
class Cart:
    items: dict[int, tuple[Product, int]] = field(default_factory=dict)

    def add_product(self, product: Product, quantity: int = 1):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("A quantidade deve ser um número inteiro.")
        if quantity <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if quantity > product.stock:
            raise ValueError("Estoque insuficiente.")
        current = self.items.get(product.id, (product, 0))[1]
        new_quantity = current + quantity
        if new_quantity > product.stock:
            raise ValueError("Estoque insuficiente.")
        self.items[product.id] = (product, new_quantity)

    def subtotal(self) -> Decimal:
        total = sum((product.price * quantity for product, quantity in self.items.values()), Decimal("0.00"))
        return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def total(self, coupon: str | None = None) -> Decimal:
        value = self.subtotal()
        if coupon == "QA10":
            value *= Decimal("0.90")
        elif coupon is not None:
            raise ValueError("Cupom inválido.")
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def checkout(self, coupon: str | None = None) -> Decimal:
        if not self.items:
            raise ValueError("Não é possível finalizar um carrinho vazio.")
        return self.total(coupon)
