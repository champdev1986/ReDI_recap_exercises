listOfWords = ['apple', 'banana', 'cherry', 'date']

def filterWordByLength(word):   
   return True if len(word)%2==0 else False

filteredList = filter(filterWordByLength, listOfWords)

print(list(filteredList))