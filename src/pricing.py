def bulk_discount(quantity):
    """Orders of 10 or more items get a 10% discount."""
    if quantity > 10:
        return 0.10
    return 0.0


def order_total(unit_price, quantity):
    """Total after the bulk discount, rounded to cents."""
    subtotal = unit_price * quantity
    return round(subtotal * (1 - bulk_discount(quantity)), 2)
