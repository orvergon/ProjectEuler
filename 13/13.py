def hmm():
    addition = 0

    while True:
        try:
            number = input()
        except Exception:
            return addition
        addition += int(number)

print(hmm())

