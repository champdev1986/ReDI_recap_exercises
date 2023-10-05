listOfNumbers = [-1, 2, -3, 4, -5]

def takeOnlyPositive(number):   
   return True if number>=0 else False

filteredList = filter(takeOnlyPositive, listOfNumbers)

print(list(filteredList))