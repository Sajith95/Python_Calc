# This is a basic Calculator

import math
import sys


def sum(Num1, Num2):
    return Num1 + Num2


def sub(Num1, Num2):
    return Num1 - Num2


def mul(Num1, Num2):
    return Num1 * Num2


def div(Num1, Num2):
    return Num1 / Num2


def sqrt(Num1):
    return Num1 ** 0.5


Num1 = float(input("Enter the First Number: "))
Operator = input("Enter the Operator (+ - * / sqrt): ")

if Operator == "sqrt":
    print("Answer: %0.3f" % sqrt(Num1))
else:
    Num2 = float(input("Enter the Second Number: "))

    if Operator == "+":
        print("Answer: ", sum(Num1, Num2))

    elif Operator == "-":
        print("Answer: ", sub(Num1, Num2))

    elif Operator == "*":
        print("Answer: ", mul(Num1, Num2))

    elif Operator == "/":
        print("Answer: ", div(Num1, Num2))

    else:
        print("Check the Operator")






