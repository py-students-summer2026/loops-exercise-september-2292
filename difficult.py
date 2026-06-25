def one():
    print("\ndifficult.one:")
    given = int(input("Enter a number: "))
    printed = []
    for i in range(2, given + 1):
            if given % i == 0:
                prime = True
                printed.append(i)
    printed.pop()
    if len(printed) > 1:
         print("The prime factors of " + str(given) + " are "+ str((printed)) + ".")
    else:
         print("There are no other prime factors.")

def two():
    print("\ndifficult.two:")
    n = int(input("Enter the term you want to calculate to: "))
    f_0 = 0
    f_1 = 1
    total = 0
    printed = []
    while total < n:
        printed.append(f_0)
        f_0, f_1 = f_1, f_0 + f_1
        total = total + 1
    print("The Fibonacci sequence up to the inputed term is " + str(printed) + ".")

def three():
    print("\ndifficult.three:")
    given = input("Enter the given string: ").lower()
    solving = input("Enter the anagram you are solving for: ").lower()
    if sorted(given) == sorted(solving):
        print("It is an anagram!")
    else:
        print("Sorry, it isn't an anagram.")



def four():
    print("\ndifficult.four:")
    n = int(input("Enter the number of terms: "))
    empty = []
    holder = 0
    while len(empty) < n:
        holder = holder + 2
        empty.append(holder)
    print("The arithmetic sequence is: "+ str(empty))

import random
def five(num):
    print("\ndifficult.five:")
    random_list = []
    for i in range(num):
        random_num = random.randint(1,100)
        random_list.append(random_num)    
    sorted_list = sorted(random_list)
    print("List: " + str(sorted_list))
    num = int(len(sorted_list) / 2)
    if len(sorted_list) % 2 == 0:
        printed = sorted_list[num-1] + sorted_list[num]
        printed = printed / 2
    else:
        num = round(num)
        printed = sorted_list[num]
    print("The median of the list is: " +str(printed))

def six(num):
    print("\ndifficult.six:")
    divisor = 0
    current = 1
    while current <= (num // 2):
        if num % current == 0:
            divisor = divisor + current
        current = current + 1
    if divisor == num and num > 0:
        print((str(num)) + " is a perfect number!")
    else:
        print((str(num)) + " is not a perfect number!")

def seven():
    print("\ndifficult.seven:")
    given = int(input("Please enter a number: "))
    total = 0
    for i in range(len(str(given))):
        divider = given % 10
        total = total + divider
        given = given // 10
    print("The total sum of the digits of the number: " + str(total) +"")

def eight(given):
    print("\ndifficult.eight:")

def nine():
    print("\ndifficult.nine:")

def ten():
    print("\ndifficult.ten:")
    printed = [2]
    empty = 2
    while len(printed) < 168:
        empty = empty + 1
        prime = True
        for i in range(len(printed)):
            if empty % printed[i] == 0:
                prime = False
                break
        if prime:
            printed.append(empty)
    print("The total sum of the prime numbers 1-1000 is " + str(sum(printed)) + ".")

