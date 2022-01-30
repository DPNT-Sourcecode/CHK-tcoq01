from solutions.CHK import checkout_solution


class TestCheckout():
    # def test_invalid_input(self):
    #     assert checkout_solution.checkout(1) == -1

    # def test_no_items(self):
    #     assert checkout_solution.checkout('') == 0

    # def test_invalid_item(self):
    #     assert checkout_solution.checkout('AB1') == -1

    # def test_no_special_offers(self):
    #     assert checkout_solution.checkout('ABCD') == 115

    # def test_with_special_offers(self):
    #     assert checkout_solution.checkout('AAAABCDB') == 260

    # def test_with_multiple_special_offers(self):
    #     assert checkout_solution.checkout('AAAAAAAAA') == 380

    # def test_with_combination_offers(self):
    #     assert checkout_solution.checkout('BEE') == 80

    # def test_with_multiple_combination_offers(self):
    #     assert checkout_solution.checkout('BBEE') == 110

    # def test_with_combination_free_item__missing(self):
    #     assert checkout_solution.checkout('EE') == 80

    # def test_with_combination_same_free_item(self):
    #     assert checkout_solution.checkout('FFF') == 20

    # def test_with_combination_same_free_item__missing(self):
    #     assert checkout_solution.checkout('FF') == 20

    # def test_with_combination_same_free_item__repeated(self):
    #     assert checkout_solution.checkout('FFFF') == 30

    def test_with_group_discount(self):
        assert checkout_solution.checkout('STXYZ') == 82

    # def test_with_group_discount__misssed(self):
    #     assert checkout_solution.checkout('ST') == 40



