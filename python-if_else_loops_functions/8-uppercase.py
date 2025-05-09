#!/usr/bin/env python3
def uppercase(str):
    majuscule = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            majuscule += chr(ord(str[i]) - 32)
            continue
        majuscule += str[i]

    print('{0}'.format(majuscule))
