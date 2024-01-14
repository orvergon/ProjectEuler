n0 = 1
n1 = 1
count = 2
while n1 < 10**999:
    aux = n1
    n1 = n1 + n0
    n0 = aux
    count += 1
    print(count)