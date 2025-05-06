#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -lastdigit
if number % 10 > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
if number % 10 == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")
if number % 10 < 6 and number % 10 != 0:
    print(
        f"Last digit of {number} is {lastdigit} and is less than 6 and not 0")
