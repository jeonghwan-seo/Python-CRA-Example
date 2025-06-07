class TaxCalculator:
    def calculate_tax(self, income: float) -> float:
        tax = 0
        tax += self._lower_bracket(income) * 0.1
        tax += self._middle_bracket(income) * 0.2
        tax += self._upper_bracket(income) * 0.3
        return tax

    def _lower_bracket(self, income: float) -> float:
        return min(income, 30000.0)

    def _middle_bracket(self, income: float) -> float:
        return min(income, 100000.0) - 30000 if income > 30000 else 0

    def _upper_bracket(self, income: float) -> float:
        return income - 100000 if income > 100000 else 0



def test_calculate_tax():
    calc = TaxCalculator()
    assert calc.calculate_tax(15000) == 1500.0
    assert calc.calculate_tax(31000) == 3200
    assert calc.calculate_tax(100200) == 17060
