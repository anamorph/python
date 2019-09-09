#!/usr/local/bin/python3
import sys

# L'opérateur m'a donné un prénom a écrire
if len(sys.argv) >= 2:
    # Cette instruction place le second argument dans la variable first_name
    first_name = sys.argv[1]
    # Cette instruction écrit le message 'Hello World !' dans la console
    print ('Hello ' + first_name + '!')

# L'opérateur ne m'a pas donné de prénom a écrire
else:
    # Cette instruction écrit le message 'Hello World !' dans la console
    print ('Hello World !')
