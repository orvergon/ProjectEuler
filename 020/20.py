from operator import mul
from functools import reduce

print(sum([int(x) for x in list(str(reduce(mul, [x for x in range(1, 101)])))]))