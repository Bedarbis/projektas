# import psutil
# print(psutil.cpu_percent())
# Print(psutil.virtual.memory())
# print(psutil.boot_time())

# arr1 = [13, 64, 15, 17, 88]
# arr2 = [23, 14, 53, 17, 80]
# # getLargerNumbers(arr1, arr2)
# print(max(arr1, arr2))

# t = input("Enter text ")
# t = t[1:-1]
# print(t)
    
# def print_smth():
#     print('Hello world!')

# n = int(input("write a number "))
# if n < 100:
#     print("False")
# else:
#     print("True")

# n = int(input("Write a number "))
# print(n >= 100)

# inputas = input("Write a word ")
# if inputas == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif inputas == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print(f"Spathiphyllum! Not {inputas}!")

# income = float(input("Enter the annual income: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# if income > 85528:
#     tax = (income - 85528)/100 * 32 + 14839.02
# # Write the rest of your code here.
# if tax < 0:
#     print("No taxes")
# else:
#     tax = round(tax, 0)
#     print("The tax is:", tax, "thalers")

# year = int(input("Enter a year: "))

# if year < 1582:
# 	print("Not within the Gregorian calendar period")
# elif year % 4 != 0:
# 	print("Common year")
# elif year % 100 != 0:
#     print("Leap year")
# elif year % 400 != 0:
#     print("Common year")
# else:
#     print("Leap year")
#     #  Write the if-elif-elif-else block here.

# Store the current largest number here.
# largest_number = -999999999
 
# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))
 
# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))
 
# # Print the largest number.
# print("The largest number is:", largest_number)

# secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)

# guess = int(input("Enter a number "))

# while True:
#     if guess != secret_number:
#         print("Ha ha! You're stuck in my loop!")
#         guess = int(input("Enter a number "))
#     else:
#         print("Well done, muggle! You are free now.")
#         break

# for i in range(2, 8):
#     print("The value of i is currently", i)

# import time
# for i in range(1, 6):
#     print(f"{i} Mississippi")
#     time.sleep(1)
# print("Ready or not, here I come!")

# inputas = input("Write a word ")
# while True:
#     if inputas != "chupacabra":
#         inputas = input("Write a word ")
#     else:
#         print("You've successfully left the loop.")
#         break

# user_word = input("Write a word ")
# user_word = user_word.upper()
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         print(letter)   

# c0 = int(input("Write a number "))
# while c0 <= 0:
#     print("Number cant be equal or lower than 0.")
#     c0 = int(input("Write a number "))
# steps = 0
# while c0 != 1:
#     print(c0)
#     if c0 % 2 == 0: 
#         c0 = c0 // 2
#     else:
#         c0 = 3 * c0 + 1
#     steps += 1
# print(c0)
# print(f"Steps = ", steps)

# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)

# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     else:
#         print(ch)

# for digit in "0165031806510":
#     if digit == "0":
#         print("x")
#         continue
#     print(digit)

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.
 
# numbers[0] = 111
# print("New list contents: ", numbers)  # Current list contents.

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.
 
# numbers[0] = 111
# print("\nPrevious list contents:", numbers)  # Printing previous list contents.
 
# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("New list contents:", numbers)  # Printing current list contents.

# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.
# replace = int(input("Write a number to change number '3' to another number "))
# hat_list[2] = replace

# # Step 2: write a line of code that removes the last element from the list.
# del hat_list[4]
# # Step 3: write a line of code that prints the length of the existing list.
# print(len(hat_list))
# print(hat_list)

my_list = []  # Creating an empty list.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)


 
    