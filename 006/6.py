max_numers = 100
square_of_sum = 0
sum_of_square = 0

for i in range(1, max_numers+1):
    square_of_sum += i
    sum_of_square += i**2
square_of_sum = square_of_sum**2
print(square_of_sum - sum_of_square)

