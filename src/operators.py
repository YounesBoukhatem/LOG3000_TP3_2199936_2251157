"""
Module contenant les opérations mathématiques de base
pour la calculatrice web.

Rôle :
    Fournir les fonctions de calcul de base : addition, soustraction,
    multiplication et division entière.
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
        Calcule la multiplication de deux nombres.
    

    Entrées :
        a (float | int) : Premier nombre.
        b (float | int) : Deuxième nombre.

    Sorties :
        float | int : Résultat de la multiplication de a et b.
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
