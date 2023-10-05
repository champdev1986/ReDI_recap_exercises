listOfWords = ['sky', 'apple', 'try']

def takeOnlyWithVowels(word):   
   return containsVowels(word)

def containsVowels(word):
   return True if set('aeiou').intersection(word) else False

filteredList = filter(takeOnlyWithVowels, listOfWords)

print(list(filteredList))