"""
Tests unitaires pour la fonction calculate() dans app.py

Rôle :
    Vérifier que la fonction analyse et évalue correctement
    les expressions mathématiques simples.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.app import calculate
import unittest

class TestCalculate(unittest.TestCase):
    """Tests pour la fonction calculate(expr)"""

    def test_addition(self):
        """Vérifie l'addition via calculate"""
        self.assertEqual(calculate("2+3"), 5)
        self.assertEqual(calculate("-1+1"), 0)
        self.assertEqual(calculate("-5+4"), -1)
        self.assertEqual(calculate("-5+-4"), -9)
        self.assertEqual(calculate("0+0"), 0)

    def test_subtraction(self):
        """Vérifie la soustraction via calculate"""
        self.assertEqual(calculate("5-2"), 3)
        self.assertEqual(calculate("0-0"), 0)
        self.assertEqual(calculate("5-6"), -1)
        self.assertEqual(calculate("-2--5"), 3)
        self.assertEqual(calculate("5--5"), 10)
        self.assertEqual(calculate("-5-5"), -10)

    def test_multiplication(self):
        """Vérifie la multiplication via calculate"""
        self.assertEqual(calculate("2*3"), 6)  
        self.assertEqual(calculate("-2*3"), -6)
        self.assertEqual(calculate("0*5"), 0)
        self.assertEqual(calculate("-2*-3"), 6)

    def test_division(self):
        """Vérifie la division via calculate"""
        self.assertEqual(calculate("6/2"), 3)
        self.assertEqual(calculate("-6/2"), -3)
        self.assertEqual(calculate("5/2"), 2) 
        self.assertEqual(calculate("9/3"), 3)  
        with self.assertRaises(ZeroDivisionError):  
            calculate("1/0")

    def test_multiple_operators(self):
        """Vérifie que les expressions avec plusieurs opérateurs échouent"""
        with self.assertRaises(ValueError):
            calculate("2+3-1")
        with self.assertRaises(ValueError):
            calculate("2*3-1")
        with self.assertRaises(ValueError):
            calculate("2*3+1")

    def test_invalid_expression(self):
        """Vérifie que les expressions vides ou invalides échouent"""
        with self.assertRaises(ValueError):
            calculate("")  
        with self.assertRaises(ValueError):
            calculate("abc+1") 
        with self.assertRaises(ValueError):
            calculate("2++3")  
        with self.assertRaises(ValueError):
            calculate("2+3*")  
        with self.assertRaises(ValueError):
            calculate("+5") 

    def test_edge_cases(self):
        """Vérifie les cas limites et atypiques"""
        self.assertEqual(calculate("0+5"), 5)  
        self.assertEqual(calculate("0-5"), -5)  
        self.assertEqual(calculate("5*0"), 0)  
        self.assertEqual(calculate("5/1"), 5)  
        self.assertEqual(calculate("-0+5"), 5)  
        self.assertEqual(calculate("-5--5"), 0)  

if __name__ == '__main__':
    unittest.main()
