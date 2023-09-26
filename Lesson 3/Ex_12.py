word = input("Enter one word: ")
def countLettersInWord(wordToCount): 
    for letter in wordToCount:
        print("Letter ", letter, " occured ", wordToCount.count(letter), " times") 

countLettersInWord(word)