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
        assert checkout_solution.checkout('AAAAAAAAA') == 380

    def test_items_with_combination_special_offers(self):
        assert checkout_solution.checkout('BEE') == 80

    def test_items_with_multi_combination_special_offers(self):
        assert checkout_solution.checkout('BBEE') == 110

    def test_items_with_combination_no_free_item(self):
        assert checkout_solution.checkout('EE') == 80

    def test_items_with_combination_same_free_item(self):
        assert checkout_solution.checkout('FFF') == 20

    def test_items_with_combination_same_free_item__missing(self):
        assert checkout_solution.checkout('FF') == 20

    def test_items_with_combination_same_free_item__repeated(self):
        assert checkout_solution.checkout('FFFF') == 30


