# name = input("Please write your name ")
# surname = input("Please write your surname ")
# age = int(input("Please write your age "))
# if age >= 21:
#     print(f"{name} {surname} are allowed to lose your money ")
# else: 
#     print("Save your parents money for something else like milk and stuff ")

# elevated_users = ["petras", "jonas", "jeronimas"]
# x = input("Please insert your username ")
 
# if x.lower() in elevated_users:
#     print(f"Welcome {x} ")
# else:
#     print(f"{x} is not in sudoers file. This incident will be reported ")

# n1 = int(input("Please write first number "))
# n2 = int(input("Please write second number "))

# if n1>n2:
#     print(f"{n1} is greater than {n2} ")
# elif n1<n2:
#     print(f"{n1} is not greater than {n2} ")
# else:
#     print(f"{n1} is equal to {n2} ")

# n1 = int(input("Write a number please "))
# n2 = int(input("Write a second number please "))
# s1 = input("Write a symbol *, /, +, - ")
# if s1=="*":
#     print(f"The answer of your multiplication is {n1*n2} ")
# elif s1=="/":
#     print(f"The answer of your division is {n1/n2} ")
# elif s1=="+":
#     print(f"The answer of your addition is {n1+n2} ")
# else:
#     print(f"The answer of your deduction is {n1-n2}")

# import random
# def guess_game():
#     number = random.randint(1, 10)
#     attempts = 0
#     max_attempts = 5
#     print("Welcome to the number guessing game")
#     print(f"Guess the number from 1 to 10 with maximum of {max_attempts} ")

#     while attempts < max_attempts:
#         try:
#             guess = int(input("Enter your guess "))
#         except ValueError:
#             print("Enter a valid number ")
#             continue
#         attempts += 1

#         if guess < 1 or guess > 10:
#             print("Please provide a number between 1 and 10 ")
#         elif guess < number:
#             print("Guess higher! ")
#         elif guess > number:
#             print("Guess lower! ")
#         else:
#             print(f"Good job dude. You made it. You guessed {number} in {attempts} attempts")
#             break
#     else:
#         print(f"Sorry you used all your {max_attempts} attempts and therefore you have failed. The correct number was {number} ")
# guess_game()

username = "admin"
password = "labas"

while True:
    x = input("Please input your username ")
    y = input("Please input your password ")
    if x == username and y == password:
        print(f"Welcome {username} ")
        break
    else:
        print("Kazka reik daryti ")
    