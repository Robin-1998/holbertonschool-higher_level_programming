#!/usr/bin/python3
for alphabet in range(100):
    if alphabet < 99:
        print("{:02d}, ".format(alphabet), end='')
# prend tout en compte sauf les deux dernier caractères dernier caractère vu
    else:
        print("{:02d}".format(alphabet))
# l'avant dernier caractère affiche le dernier mot mais sans la virgule
