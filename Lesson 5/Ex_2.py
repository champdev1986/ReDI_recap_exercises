def capitalizeWord(myString):
    return myString.capitalize()

def capitalizeAllWords(listOfWords):
    print(list(map(capitalizeWord, listOfWords)))

capitalizeAllWords(['apple', 'banana', 'cherry'])
