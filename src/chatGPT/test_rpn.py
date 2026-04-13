import unittest
from rpn import rpn_eval, RPNError

class TestRPN(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(rpn_eval("3 4 +"), 7)

    def test_resta(self):
        self.assertEqual(rpn_eval("5 3 -"), 2)

    def test_multiplicacion(self):
        self.assertEqual(rpn_eval("3 4 *"), 12)

    def test_division(self):
        self.assertEqual(rpn_eval("10 2 /"), 5)

    def test_division_por_cero(self):
        with self.assertRaises(RPNError):
            rpn_eval("3 0 /")

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            rpn_eval("+")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            rpn_eval("3 4 ?")

    def test_pila_final(self):
        with self.assertRaises(RPNError):
            rpn_eval("3 4")

    def test_sqrt(self):
        self.assertEqual(rpn_eval("9 sqrt"), 3)

    def test_sqrt_negativo(self):
        with self.assertRaises(RPNError):
            rpn_eval("-4 sqrt")

    def test_constantes(self):
        import math
        self.assertAlmostEqual(rpn_eval("p"), math.pi)

    def test_dup(self):
        self.assertEqual(rpn_eval("3 dup *"), 9)

    def test_swap(self):
        self.assertEqual(rpn_eval("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(rpn_eval("3 4 drop"), 3)

    def test_memoria(self):
        self.assertEqual(rpn_eval("5 0 STO 0 RCL"), 5)
    def test_chs(self):
        self.assertEqual(rpn_eval("3 chs"), -3)

    def test_ln(self):
        import math
        self.assertAlmostEqual(rpn_eval("1 ln"), 0)

    def test_sin(self):
        import math
        self.assertAlmostEqual(rpn_eval("90 sin"), 1)

    def test_cos(self):
        self.assertAlmostEqual(rpn_eval("0 cos"), 1)

    def test_yx(self):
        self.assertEqual(rpn_eval("2 3 yx"), 8)

if __name__ == "__main__":
    unittest.main()