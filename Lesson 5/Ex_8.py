def reverseWord(myWord):
    return myWord[::-1]

def reverseAllWords(listOfWords):
    print(list(map(reverseWord, listOfWords)))

reverseAllWords(['apple', 'banana'])