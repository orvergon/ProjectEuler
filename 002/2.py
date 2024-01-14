x, y = (1, 1)
aux = None
soma = 0

while y < 4_000_000:
    aux = x + y
    x = y
    y = aux
    if y%2 == 0:
        soma += y
        print("%d - %d"%(y, soma))
    else:
        print(y)

