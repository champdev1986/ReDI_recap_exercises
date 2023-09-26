# list = [1,2,3,10,4,5,6]

# 1
# def getSum (listOfNumbewrs):
#     result = 0
#     for number in listOfNumbewrs:
#         result = result + number
#     return result

# print ("Result = ", getSum(list))

# 2
# def getHighestNumber(listOfNumbewrs):
#     listOfNumbewrs.sort()
#     return listOfNumbewrs[-1]

# print("Highest is = ", getHighestNumber(list))

# 3
# listOfFruits = list()
# listOfFruits.insert(0, "Apple")
# listOfFruits.insert(1, "Pear")
# listOfFruits.append("Cherry")
# listOfFruits.append("Kiwi")
# listOfFruits.sort()
# listOfFruits.remove(listOfFruits[1])
# print ("List of fruits: ", listOfFruits[::])

# 4
# def isListEmty(list):
#     return not list

# print("Is list empty: ", isListEmty(listOfFruits))

# print("Is list empty: ", len(listOfFruits)==0)

# 5
# fiveItemsList = [3, 4, "Apple", 8, "Kiwi"]

# def reverseList(list):
#     list.reverse()
#     return list

# print ("Reversed list: ", reverseList(fiveItemsList[::]))

# 6
# word = input("Enter the word please: ").lower()
# i = len(word) - 1
# reversed_word = ""
# while i >= 0:
#     reversed_word = reversed_word + word[i]
#     i-=1
# if reversed_word == word:
#     print("Your input word is palindrome")
# else:
#     print("Reversed word = ", reversed_word)

# 7
# fiveNumbersList = [2,4,6,8,10]
# newList = list()
# for number in fiveNumbersList:
#     newList.append(number**2)
# print("New list = ", newList)

# 8
# number = int(input("Enter a number: "))
# my_range = range(1,number+1)
# result = 0
# for i in my_range:
#     result+=i
# print(result)

# 9
# number_from_user = int(input("Please input a number: "))
# is_prime_number = True

# for i in range(2, number_from_user):
#     if (number_from_user % i ) == 0:
#         is_prime_number = False

# if is_prime_number:
#     print(f"{number_from_user} is a prime number")
# else:
#     print(f"{number_from_user} is not a prime number")

# 10
# for i in range(0, 20, 3):
#     if i == 0 continue
#     print(i) 
