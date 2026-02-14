"""
Module principal du serveur Flask pour la calculatrice web.

Rôle :
    Initialise le serveur Flask, définit les routes HTTP,
    et traite les expressions mathématiques envoyées par le frontend
    en utilisant les fonctions du module operators.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire associant chaque symbole d'opération à la fonction correspondante
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """
    Rôle :
        Analyse et évalue une expression mathématique simple
        contenant un seul opérateur (+, -, *, /) et deux opérandes numériques.

    Entrées :
        expr (str) : Expression mathématique sous forme de chaîne
                     (ex: "3+4", "10 / 2").

    Sorties :
        float | int : Résultat de l'opération effectuée.

    Erreurs relevées :
        ValueError : 
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
        a = float(left)  # Conversion en float pour permettre les décimales
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Appel dynamique de la fonction associée à l'opérateur
    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Rôle :
        Gère la route principale de l'application web.
        Affiche la page de la calculatrice (GET) ou
        évalue l'expression saisie par l'utilisateur (POST).

    Entrées :
        Méthode HTTP via Flask :
            - GET : Aucun paramètre supplémentaire
            - POST : Formulaire contenant la clé "display" avec l'expression

    Sorties :
        str : Page HTML rendue avec le résultat calculé
              ou un message d'erreur si l'évaluation échoue.
    """

    result = ""

    if request.method == 'POST':
        expression = request.form.get('display', '')

        try:
            result = calculate(expression)
        except Exception as e:
            # Affiche l'erreur à l'utilisateur
            result = f"Error: {e}"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    """
    Rôle :
        Lance le serveur Flask en mode debug pour le développement.
    
    Entrées :
        Aucune.

    Sorties :
        Lancement du serveur Flask accessible sur localhost:5000
    """
    app.run(debug=True)
