from unittest import TestCase
from evaluator import Evaluator


class TestEvaluator(TestCase):
    def test_evaluate_simple(self):
        self.assertEqual(Evaluator.simple_eval('(0.5 +0.8-0.2)* 2'), ' = 2.2')
        self.assertEqual(Evaluator.simple_eval('5**2 \n'), ' = 25')
        self.assertEqual(Evaluator.simple_eval('1/4'), ' = 0.25')

    def test_evaluate_medium_operations(self):
        self.assertEqual(Evaluator.simple_eval('4^2'), ' = 16')
        self.assertEqual(Evaluator.simple_eval('4/2'), ' = 2')
        self.assertEqual(Evaluator.simple_eval('10*30%'), ' = 3')
        self.assertEqual(Evaluator.simple_eval('5!'), ' = 120')

    def test_equals_sign(self):
        self.assertEqual(Evaluator.simple_eval('3+4 = '), '7')

    def test_junk_before(self):
        self.assertEqual(Evaluator.simple_eval('so we have 3+4'), ' = 7')
        self.assertEqual(Evaluator.simple_eval('Thus, we get: 3+4='), '7')

    def test_advanced_simple(self):
        self.assertEqual(Evaluator.advanced_eval_wrapper('(0.5 +0.8-0.2)* 2'), ' = 2.2')
        self.assertEqual(Evaluator.advanced_eval_wrapper('5**2 \n'), ' = 25')
        self.assertEqual(Evaluator.advanced_eval_wrapper('1/4'), ' = 0.25')
        self.assertEqual(Evaluator.advanced_eval_wrapper('4/2'), ' = 2')
        self.assertEqual(Evaluator.advanced_eval_wrapper('3+4 = '), '7')

    def test_advanced_depth1(self):
        self.assertIn('1.7917', Evaluator.advanced_eval_wrapper('ln(6)'))
        self.assertIn('2.8414', Evaluator.advanced_eval_wrapper('sin(1)+2'))

    def test_advanced_factorial(self):
        self.assertEqual(Evaluator.advanced_eval_wrapper('5!'), ' = 120')
        self.assertEqual(Evaluator.advanced_eval_wrapper('log2((4*4))!'), ' = 24')
        self.assertEqual(Evaluator.advanced_eval_wrapper('log2(2!)!'), ' = 1')
        self.assertRaises(ValueError, Evaluator.advanced_eval_wrapper, 'ln(5)!')

    def test_advanced_deep(self):
        self.assertIn('0.8905', Evaluator.advanced_eval_wrapper('sin(ln(3))'))

    def test_advanced_mix(self):
        self.assertEqual(Evaluator.advanced_eval_wrapper('(5! + 6)*0.3'), ' = 37.8')
        self.assertIn('5.8905', Evaluator.advanced_eval_wrapper('3+sin(ln(3))+2'))
        self.assertIn('2.8414', Evaluator.advanced_eval_wrapper('(sin((1))+2)'))
