#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if number < 0:
    lastdig = -(lastdig)
thestring = "Last digit of {} is {}".format(number, lastdig)
if lastdig > 5:
    print(f"{thestring} and is greater than 5")
elif lastdig == 0:
    print(f"{thestring} and is 0")
elif lastdig < 6:
    print(f"{thestring} and is less than 6 and not 0")
