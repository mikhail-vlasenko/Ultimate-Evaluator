from unittest import TestCase
from evaluator import Evaluator


class TestEvaluator(TestCase):
    def test_evaluate_simple(self):
        self.assertEqual(Evaluator.evaluate('(0.5 +0.8-0.2)* 2'), ' = 2.2')
        self.assertEqual(Evaluator.evaluate('5**2 \n'), ' = 25')
        self.assertEqual(Evaluator.evaluate('1/4'), ' = 0.25')

    def test_equals_sign(self):
        self.assertEqual(Evaluator.evaluate('3+4 = '), '7')

    def test_junk_before(self):
        self.assertEqual(Evaluator.evaluate('so we have 3+4'), ' = 7')
        self.assertEqual(Evaluator.evaluate('Thus, we get: 3+4='), '7')

    def test_advanced_simple(self):
        self.assertEqual(Evaluator.advanced_eval_wrapper('(0.5 +0.8-0.2)* 2'), ' = 2.2')

    def test_advanced_depth1(self):
        self.assertIn('1.7917', Evaluator.advanced_eval_wrapper('ln(6)'))
        self.assertIn('0.8414', Evaluator.advanced_eval_wrapper('sin(1)'))

    def test_advanced_deep(self):
        self.assertIn('0.8905', Evaluator.advanced_eval_wrapper('sin(ln(3))'))

