"""
Module principal du serveur Flask pour la calculatrice web.

Ce module :
- Initialise l'application Flask
- Définit les routes HTTP
- Traite les expressions mathématiques envoyées par le frontend
- Utilise les fonctions du module operators pour effectuer les calculs
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire associant chaque symbole d'opération
# à la fonction correspondante dans le module operators
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """
    Analyse et évalue une expression mathématique simple.

    L'expression doit contenir :
    - Deux opérandes numériques
    - Un seul opérateur parmi +, -, *, /

    Paramètres:
        expr (str): Expression mathématique sous forme de chaîne
                    (ex: "3+4", "10 / 2").

    Retour de fonction:
        float | int: Résultat de l'opération effectuée.

    Erreurs relevées:
        ValueError:
            - Si l'expression est vide ou invalide.
            - Si plusieurs opérateurs sont présents.
            - Si les opérandes ne sont pas des nombres.
            - Si le format de l'expression est incorrect.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Suppression des espaces pour simplifier l'analyse
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de l'opérateur dans la chaîne
    for i, ch in enumerate(s):
        if ch in OPS:
            # Vérifie qu'un seul opérateur est présent
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l'opérateur n'est ni au début ni à la fin
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        # Conversion en float pour permettre les décimales
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Appel dynamique de la fonction associée à l'opérateur
    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gère la route principale de l'application web.

    Méthodes supportées:
        - GET : Affiche la page de la calculatrice.
        - POST : Récupère l'expression saisie par l'utilisateur,
                 appelle la fonction calculate et affiche le résultat.

    Retour de fonction:
        str: Page HTML rendue avec ou sans résultat.
    """

    result = ""

    if request.method == 'POST':
        # Récupère l'expression saisie dans le champ "display"
        expression = request.form.get('display', '')

        try:
            result = calculate(expression)
        except Exception as e:
            # Capture les erreurs pour les afficher proprement à l'utilisateur
            result = f"Error: {e}"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    # Lancement du serveur en mode debug pour le développement
    app.run(debug=True)
