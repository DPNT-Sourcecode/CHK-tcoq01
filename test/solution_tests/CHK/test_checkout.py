from solutions.CHK import checkout_solution


class TestCheckout():
    def test_no_items(self):
        assert checkout_solution.checkout('') == 0
