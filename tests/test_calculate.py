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
    """Tests pour calculate(expr)"""

    def test_addition(self):
        """Rôle : Vérifie l'addition via calculate
        Entrées : "2+3"
        Sorties : 5"""
        self.assertEqual(calculate("2+3"), 5)

    def test_subtraction(self):
        """Rôle : Vérifie la soustraction via calculate
        Entrées : "5-2"
        Sorties : 3"""
        self.assertEqual(calculate("5-2"), 3)

    def test_multiple_operators(self):
        """Rôle : Vérifie que les expressions avec plusieurs opérateurs échouent
        Entrées : "2+3-1"
        Erreurs relevées : ValueError"""
        with self.assertRaises(ValueError):
            calculate("2+3-1")

    def test_invalid_expression(self):
        """Rôle : Vérifie que les expressions vides ou invalides échouent
        Entrées : ""
        Erreurs relevées : ValueError"""
        with self.assertRaises(ValueError):
            calculate("")
