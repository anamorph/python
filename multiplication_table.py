#!/usr/local/bin/python3
import sys

# L'opérateur m'a donné un nombre a multiplier
number = int(input('Which number should I multiply ?\n'))
# Je crée une boucle pour calculer la table de multiplication de 1 à 10 pour ce nombre
for multiplier in range(1,11):
    # Cette instruction écrit la multiplication du nombre par un multiplicateur de 1 à 10 dans la console
    print(number,'x',multiplier,'=',number*multiplier)