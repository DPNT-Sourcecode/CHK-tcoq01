from solutions.CHK import checkout_solution


class TestCheckout():
    def test_invalid_input(self):
        assert checkout_solution.checkout(1) == -1

    def test_no_items(self):
        assert checkout_solution.checkout('') == 0

    def test_invalid_item(self):
        assert checkout_solution.checkout('ABZ') == -1

    def test_items_no_special_offers(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_items_with_special_offers(self):
        assert checkout_solution.checkout('AAAABCDB') == 260

    def test_items_with_multiple_special_offers(self):
        assert checkout_solution.checkout('BBEE') == 110
