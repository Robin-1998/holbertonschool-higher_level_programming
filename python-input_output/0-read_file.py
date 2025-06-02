#!/usr/bin/python3
def read_file(filename=""):
    f = open('filename', 'w', encoding="utf-8")
    with open('filename', encoding="utf-8") as f:
        read_file = f.read
    f.closed
True
