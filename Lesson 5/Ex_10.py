listOfNumbers = [10, 15, 20, 25, 88, 100]
givenNumber = 5

def takeIfDividesByNumber(number):   
   return True if number % givenNumber == 0 else False

filteredList = filter(takeIfDividesByNumber, listOfNumbers)

print(list(filteredList))