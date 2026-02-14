"""
Module contenant les opérations mathématiques de base
pour la calculatrice web.

Fonctions disponibles :
- add : addition
- subtract : soustraction
- multiply : multiplication
- divide : division
"""

def add(a, b):
    """
    Calcule la somme de deux nombres.

    Args:
        a (float | int): Premier nombre.
        b (float | int): Deuxième nombre.

    Retour de fonction:
        float | int: Résultat de l'addition de a et b.
    """
    return a + b


def subtract(a, b):
    """
    Calcule la différence entre deux nombres.

    Args:
        a (float | int): Premier nombre.
        b (float | int): Deuxième nombre.

    Retour de fonction:
        float | int: Résultat de la soustraction (b - a).
    """
    return b - a


def multiply(a, b):
    """
    Calcule la puissance d’un nombre par un autre.

    Note:
        Cette fonction utilise l’opérateur **,
        ce qui élève 'a' à la puissance 'b'.

    Args:
        a (float | int): Base.
        b (float | int): Exposant.

    Retour de fonction:
        float | int: Résultat de a élevé à la puissance b.
    """
    return a ** b


def divide(a, b):
    """
    Effectue une division entière entre deux nombres.

    Note:
        Utilise l’opérateur // pour effectuer une division entière.

    Args:
        a (float | int): Numérateur.
        b (float | int): Dénominateur.

    Retour de fonction:
        int: Résultat de la division entière de a par b.

    Erreur relevée:
        ZeroDivisionError: Si b est égal à 0.
    """
    return a // b
