def square(n):
    return n*n

def double(n):
    return n+n

def squareElements(listOfNumbers):
    print(list(map(square, map(double, listOfNumbers))))

squareElements([1, 2, 3])