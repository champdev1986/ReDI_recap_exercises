word = input("Enter one word: ")
def findFirstMiddleAndLastChar(wordToFind): 
    print("First: ", wordToFind[0], " middle: ", wordToFind[round(len(wordToFind)/2)], " last: ", wordToFind[len(wordToFind)-1]) 

findFirstMiddleAndLastChar(word)