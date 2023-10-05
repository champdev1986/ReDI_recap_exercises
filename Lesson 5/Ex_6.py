from functools import reduce

words = ['apple', 'banana', 'cherry']

print(reduce(lambda a,b: a+" "+b, words))