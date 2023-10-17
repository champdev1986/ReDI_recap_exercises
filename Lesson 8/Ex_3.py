from functools import reduce

def convertListItemsToIntegers(list):
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

def calculateAverage():
    input_string = input('Enter integers separated by space: \n')
    listOfIntegers = input_string.split()
    try:
        listOfIntegers = convertListItemsToIntegers(listOfIntegers)
    except Exception as error:
        print(error)
    else:
        average = (reduce(lambda a,b: a+b, listOfIntegers)) / len(listOfIntegers)
        print("The average value of your numbers is: " + str(average))




calculateAverage()