word = "thequickbrownfoxjumpsoverthelazydog"
letter = input("Please, enter one letter: ")

def countLetterOccurance(wordToSearch, letterToCount):    
    print(f"The letter {letterToCount} occured {wordToSearch.count(letterToCount)} times")

countLetterOccurance(word, letter)

