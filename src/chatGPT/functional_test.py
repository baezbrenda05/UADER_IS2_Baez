import unittest
from rpn import rpn_eval, RPNError

class TestFuncional(unittest.TestCase):

    def test_caso1_cli(self):
        # Caso 1: operacion basica suma
        self.assertEqual(rpn_eval("3 4 +"), 7)

    def test_caso2_multiple_operadores(self):
        # Caso 2: multiples operadores
        self.assertEqual(rpn_eval("5 1 2 + 4 * + 3 -"), 14)

    def test_caso3_constantes_y_funciones(self):
        # Caso 3: constantes y funciones avanzadas
        self.assertAlmostEqual(rpn_eval("3 2 yx 9 sqrt +"), 12)

    def test_caso4_division_por_cero(self):
        # Caso 4: division por cero
        with self.assertRaises(RPNError):
            rpn_eval("3 0 /")

if __name__ == "__main__":
    unittest.main()