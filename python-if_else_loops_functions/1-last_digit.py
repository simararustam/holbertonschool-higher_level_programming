#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_dig = str(number)[-1:]
else:
    last_dig = str(number)[:2]

last_dig = int(last_dig)

if last_dig > 5:
    print(f"Last digit of {number} is {last_dig} and is greater than 5")
elif last_dig == 0:
    print(f"Last digit of {number} is {last_dig} and is 0")
else:
    print(f"Last digit of {number} is {last_dig} and is less than 6 and not 0")
