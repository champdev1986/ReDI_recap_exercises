
def readFile():
    try:
        with open("Lesson 8/example.txt", "r") as file:
            content = file.read()
            print(content)
    except IOError as error:
        print(type(error))
    else:
        print("Everything works well")
    finally:
        print("Finally block")

readFile()