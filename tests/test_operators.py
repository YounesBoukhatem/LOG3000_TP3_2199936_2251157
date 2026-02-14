"""
Tests unitaires pour le module operators.

Rôle :
    Vérifier que toutes les fonctions mathématiques de base
    retournent les résultats attendus.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.operators import add, subtract, multiply, divide
import unittest


class TestOperators(unittest.TestCase):
    """Test des fonctions de operators.py"""

    def test_add(self):
        """Rôle : Vérifie que l'addition fonctionne correctement
        Entrées : valeurs numériques a et b
        Sorties : résultat correct de a + b"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, 4), -1)
        self.assertEqual(add(-5, -4), -9)

    def test_subtract(self):
        """Rôle : Vérifie la soustraction (b - a)
        Entrées : valeurs numériques a et b
        Sorties : résultat correct de b - a"""
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 6), -1)
        self.assertEqual(subtract(-2, -5), 3)
        self.assertEqual(subtract(5, -5), 10)
        self.assertEqual(subtract(-5, 5), -10)

    def test_multiply(self):
        """Rôle : Vérifie la multiplication (exposant)
        Entrées : valeurs numériques a et b
        Sorties : résultat correct de a ** b"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(4, -1), -4)
        self.assertEqual(multiply(-4, -1), 4)

    def test_divide(self):
        """Rôle : Vérifie la division entière
        Entrées : valeurs numériques a et b
        Sorties : résultat correct de a // b
        Erreurs relevées : ZeroDivisionError si b = 0"""
        self.assertEqual(divide(5, 2), 2)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        self.assertEqual(divide(-6, 2), -3)
        self.assertEqual(divide(8, -2), -4)
