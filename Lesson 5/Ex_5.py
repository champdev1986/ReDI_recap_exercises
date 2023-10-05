from functools import reduce

prices = [1, 2, 3, 4]

print(reduce(lambda a,b: a*b, prices))