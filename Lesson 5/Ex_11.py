from functools import reduce

words = ['apple', 'banana', 'cherry']

print(reduce(lambda a,b: len(a)>len(b), words))