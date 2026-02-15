"""
Module contenant les opérations mathématiques de base
pour la calculatrice web.

Rôle :
    Fournir les fonctions de calcul de base : addition, soustraction,
    multiplication (actuellement exposant) et division entière.
"""

def add(a, b):
    """
    Rôle :
        Calcule la somme de deux nombres.

    Entrées :
        a (float | int) : Premier nombre.
        b (float | int) : Deuxième nombre.

    Sorties :
        float | int : Résultat de l'addition de a et b.
    """
    return a + b


def subtract(a, b):
    """
    Rôle :
        Calcule la différence entre deux nombres.

    Entrées :
        a (float | int) : Premier nombre.
        b (float | int) : Deuxième nombre.

    Sorties :
        float | int : Résultat de la soustraction (b - a).
    """
    return a - b


def multiply(a, b):
    """
    Rôle :
        Calcule la puissance d’un nombre par un autre.
        (Note : actuellement la fonction élève 'a' à la puissance 'b',
        au lieu de faire une multiplication classique.)

    Entrées :
        a (float | int) : Base.
        b (float | int) : Exposant.

    Sorties :
        float | int : Résultat de a élevé à la puissance b.
    """
    return a * b


def divide(a, b):
    """
    Rôle :
        Effectue une division entière entre deux nombres.

    Entrées :
        a (float | int) : Numérateur.
        b (float | int) : Dénominateur.

    Sorties :
        int : Résultat de la division entière de a par b.

    Erreurs relevées :
        ZeroDivisionError : Si b est égal à 0.
    """
    return a // b
