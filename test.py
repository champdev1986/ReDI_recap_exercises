def sum(x, y):
    result = (x+2)*(y-3)
    print ("Result = " + str(result))
    return result

def result (i):
    if(i<0): print ("the result is negative")


sum(3, 1)
result(sum(3,2))


def enterName (name):
    print ("Hello, " + name + "!")

def enterNumbers (a,b):
    print (str(a*b))

enterName("Yevhen")
enterNumbers(3,4)

name = input("What's your name: ")
print(f"Hello, {name}")

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
result = numberOne*numberTwo
print("Result: ", result)
