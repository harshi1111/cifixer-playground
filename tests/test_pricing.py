from pricing import bulk_discount, order_total


def test_small_order_has_no_discount():
    assert bulk_discount(3) == 0.0


def test_ten_items_get_the_discount():
    assert bulk_discount(10) == 0.10


def test_order_total():
    assert order_total(5.0, 10) == 45.0
