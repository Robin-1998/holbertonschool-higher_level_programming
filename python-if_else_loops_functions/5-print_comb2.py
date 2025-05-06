#!/usr/bin/python3
for alphabet in range(100):
    if alphabet < 99:
        print(f"{alphabet:02d}, ", end='')
#prend tout en compte sauf les deux dernier caractères dernier caractère vu
    else:
        print(f"{alphabet:02d}")
#l'avant dernier caractère affiche le dernier mot mais sans la virgule
