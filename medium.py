import random

def one():
    """
    Write a program that finds the largest element in a given list using a for loop.
    """
    print("\nmedium.one:")
    given = input("Please enter a list (separated by spaces): ").split()
    given_list = []
    for i in range(len(given)):
        given_list.append(given[i])
    largest = given_list[0]
    for i in range(len(given_list)):
        if given_list[i] > largest:
            largest = given_list[i]
    print(str(largest) + " is the largest element in this list.")

def two():
    print("\nmedium.two:")
    given = input("Please enter a list (separated by spaces): ").split()
    given_list = []
    for i in range(len(given)):
        given_list.append(given[i])
    n = len(given_list)
    i = 0
    empty = 0
    while n > 0:
        empty = empty + int(given_list[i])
        i = i + 1
        n = n - 1
    empty = empty / len(given_list)
    print("The average of the list is " + str(empty) + ".")

def three():
    print("\nmedium.three:")

    string_input = list(input("Please input a string: "))
    reverse = string_input[::-1]
    n = len(string_input)
    for i in range(n//2):
        if string_input[i] != reverse[i]:
            print("Not a palindrome!")
            break
        else:
            print("This is a palindrome!")
            break

def four():
    print("\nmedium.four:")
    number = int(input("Please input the first number: "))
    n = int(input("How many terms do you want to find? "))
    empty_list = []
    for i in range(n):
        empty_list.append(number)
        number = number * 2
    print(empty_list)

def five(limit):
    print("\nmedium.five:")
    random_list = []
    for i in range(limit):
        random_num = random.randint(1,100)
        random_list.append(random_num)
    print(random_list)
    initial = random_list[0]
    largest = 0
    for i in range(limit):
        if random_list[i] > largest:
            initial = largest
            largest = random_list[i]
    print(str(initial) + " is the second largest element in this list.")

def six(given):
    print("\nmedium.six:")
    n = given 
    printed = 1
    while n != 0:
        printed = printed * n
        n = n - 1
    print("The factorial of " +str(given) + " is " + str(printed) +".")

def seven():
    print("\nmedium.seven:")

    given = int(input("Enter a number: "))
    for i in range(given):
        squared = i**2
        if squared == given:
            print(str(given) + " is a perfect square!")
            break
        if squared > given:
            print(str(given) + " is not a perfect square!")
            break

def eight(given):
    print("\nmedium.eight:")
    printed = [2]
    empty = 2
    while len(printed) <= given:
        empty = empty + 1
        prime = True
        for i in range(len(printed)):
            if empty % printed[i] == 0:
                prime = False
                break
        if prime:
            printed.append(empty)
    print("The total sum of the prime numbers 1-100 is " + str(sum(printed)) + ".")

def nine():
    print("\nmedium.nine:")
    given = input("Enter a sentence: ")
    delimiters = [',','.','!','?']
    for i in delimiters:
        new = given.replace(i,"")
    printed = new.split()
    print("Total words in sentence: " + str(len(printed)))

def ten(list_1, list_2):
    print("\nmedium.ten:")
    i = 0
    printed = []
    while i < len(list_1):
        compare = list_1[i]
        if compare in list_2:
            printed.append(compare)
        i = i + 1
    print("Common values: " + str(printed))


