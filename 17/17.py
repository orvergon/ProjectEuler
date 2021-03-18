from math import floor

unidades = {0:"",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"}

teens = {10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen"}

dezenas = {20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety"}

magnitudes = {100:"hundred",
        1000: "thousand",
        1000000: "million"}

def writeNumberRecursive(number:int, magnitude:int) -> str:
    if magnitude == 0:
        return unidades[number]
    elif magnitude == 1:
        if number < 20:
            return teens[number]
        else:
            dezena = (number // 10) * 10
            name_dezena = dezenas[dezena]
            rest = number - dezena
            if rest == 0:
                return name_dezena
            else:
                return name_dezena + "" + writeNumberRecursive(rest, 0)
    elif magnitude == 2:
        name = writeNumberRecursive((number // 100), 0) + "" + magnitudes[100]
        rest = number % 100
        if rest == 0:
            return name
        else:
            return name + "and" + writeNumberRecursive(rest, getNumberMagnitude(rest))
    elif magnitude == 3:
        name = writeNumberRecursive((number // 1000), 0) + "" + magnitudes[1000]
        rest = number % 1000
        if rest == 0:
            return name
        else:
            return name + "" + writeNumberRecursive(rest, getNumberMagnitude(rest))

def getNumberMagnitude(number:int) -> int:
    for i in range(0, 4):
        if (10**i) <= number < (10**(i+1)):
            return i


def writeNumber(number:int) -> str:
    return writeNumberRecursive(number, getNumberMagnitude(number))

total = 0
for x in range(1, 1001):
    total += len(writeNumber(x))
print(total)

