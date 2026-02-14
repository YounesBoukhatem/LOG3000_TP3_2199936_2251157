# Répertoire de tests

Ce dossier contient les tests unitaires pour le projet Calculatrice Web.

## Structure

- `__init__.py` : rend le dossier testable comme package Python.
- `test_operators.py` : tests des fonctions mathématiques de `operators.py`.
- `test_calculate.py` : tests de la fonction `calculate()` de `app.py`.

## Exécution des tests

1. Installer `unittest` (inclus avec Python).
2. Depuis la racine du projet, exécuter : python -m unittest discover -s tests -p "*.py" -v


