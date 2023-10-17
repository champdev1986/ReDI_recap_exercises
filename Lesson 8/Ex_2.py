def countWords():
    try:
        sentence = input("Enter a sentence: ")
        print(len(sentence.split()))
    except TypeError:
        print("TypeError")
    except ValueError:
        print("ValueError")
    else:
        print("Everything works well")
    finally:
        print("Finally block")


countWords()