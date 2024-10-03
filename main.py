import json

# Création du contenu du notebook Jupyter pour l'exercice sur le circuit dérivateur

notebook_content_4 = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Circuit Dérivateur : Analyse et Résolution\n",
                "Dans ce notebook, nous analysons un circuit électrique composé d'une résistance \(R\) et d'une capacité \(C\), appelé **circuit dérivateur**. Nous dériverons l'équation différentielle gouvernant le comportement du circuit et étudierons la réponse du circuit pour une tension d'entrée constante."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Équation différentielle pour la charge \( q(t) \)\n",
                "Pour un circuit RC en série, la loi des mailles de Kirchhoff donne :\n",
                "\\[ V_e(t) = V_R(t) + V_C(t) \\]\n",
                "où :\n",
                "- \( V_e(t) \) est la tension d'entrée,\n",
                "- \( V_R(t) = R \cdot i(t) \) est la tension aux bornes de la résistance,\n",
                "- \( V_C(t) = \\frac{q(t)}{C} \) est la tension aux bornes du condensateur.\n",
                "\n",
                "Le courant \( i(t) \) est lié à la charge \( q(t) \) par :\n",
                "\\[ i(t) = \\frac{dq(t)}{dt} \\]\n",
                "Donc, l'équation différentielle devient :\n",
                "\\[ V_e(t) = R \\cdot \\frac{dq(t)}{dt} + \\frac{q(t)}{C} \\]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Comportement lorsque \( RC \) tend vers 0\n",
                "Lorsque \( RC \) tend vers 0, l'équation se simplifie en :\n",
                "\\[ V_e(t) \\approx R \\cdot \\frac{dq(t)}{dt} \\]\n",
                "et on a :\n",
                "\\[ \\frac{V_s(t)}{RC} = \\frac{dV_e(t)}{dt} \\]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Résolution de l'équation différentielle avec conditions initiales\n",
                "L'équation différentielle est :\n",
                "\\[ V_e(t) = R \\cdot \\frac{dq(t)}{dt} + \\frac{q(t)}{C} \\]\n",
                "Avec la condition initiale \( q(0) = 0 \), on résout :\n",
                "\\[ q(t) = V_0 C \\left( 1 - e^{-\\frac{t}{RC}} \\right) u(t) \\]\n",
                "La tension aux bornes de la résistance est :\n",
                "\\[ V_s(t) = V_0 e^{-\\frac{t}{RC}} u(t) \\]\n",
                "Donc :\n",
                "\\[ \\frac{V_s(t)}{RC} = \\frac{V_0}{RC} e^{-\\frac{t}{RC}} u(t) \\]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Limite lorsque \( RC \) tend vers 0\n",
                "Lorsque \( RC \) tend vers 0, la fonction se comporte comme :\n",
                "\\[ \\lim_{RC \\to 0} \\frac{V_s(t)}{RC} = V_0 \\delta(t) \\]\n",
                "où \( \\delta(t) \\) est la distribution de Dirac."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Conclusion\n",
                "Nous avons montré que, pour un circuit dérivateur, lorsque \( RC \) tend vers 0, la sortie du circuit tend à devenir proportionnelle à la dérivée de la tension d'entrée. Ceci est illustré par la convergence vers la distribution de Dirac."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.10"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

# Enregistrement du notebook dans un fichier
notebook_filename_4 = "/mnt/data/Circuit_Derivateur_Resolution.ipynb"

with open(notebook_filename_4, 'w', encoding='utf-8') as f:
    json.dump(notebook_content_4, f)

notebook_filename_4
