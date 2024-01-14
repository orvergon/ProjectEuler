from math import sqrt

target = 1000
for a in range(1, target):
    for b in range(1, target):
        c = sqrt((a**2) + (b**2))
        if (a + b + c) == target:
            print(f"{a}² + {b}² = {c}²")

