def square(n):
    return n*n

def squareElements(listOfNumbers):
    print(list(map(square, listOfNumbers)))

squareElements([1, 2, 3, 4])