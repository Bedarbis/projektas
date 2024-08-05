# input random
# get_random_number() 
# print_smth()

# def even_odd(num):
    
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(10))

# def print_smth():
#     print('Hello world!')
# print_smth()

# import random

# def get_random_number():
#     print(random.randint(0, 10))
# get_random_number()

# def find_sum(num1, num2):
#     num1 + num2 
     
# find_sum(5, 10)

# my_list = ["pirmas", "antras", "trecias", "ketvirtas", "penktas"]

# def add_string(list):
#     new_list = []
#     for word in list:
#         new_list.append(word + ".string")
#     return new_list

# appended = add_string(my_list)
# print(appended)

# def calculate():
#     num1 = int(input("Input first number "))
#     num2 = int(input("Input second number "))

#     sum = num1 + num2
#     sub = num1 - num2
#     if num2 != 0:
#         div = num1 / num2
#     else:
#         div = None
#     multi = num1 * num2

#     print(f"Sum of number {num1} and number {num2} is {sum}")
#     print(f"Subtraction of number {num1} and number {num2} is {sub}")
#     if num2 !=0:
#         print(f"Division of number {num1} and number {num2} is {div}")
#     else:
#         print(f"The world has ended because of you. You tried to devide by zero. ")
#     print(f"Multiplication of number {num1} and number {num2} is {multi}")
# calculate()

# def greet(name: str) -> str:
#     return f"Hello {name}"

# print(greet("Grybas"))

# Define math function

# def math(a: int, b: int) -> int:
#     addition = a + b
#     subtract = a - b
#     division = a / b
#     multiply = a * b
#     return addition, subtract, division, multiply
# def get_user_number() -> int:
#     while True:
#         user_input = input("Inser a number ")
#         if not user_input.isdigit():
#             print("The value is not a number, please try again")
#             continue
#         else:
#             user_input1 = int(user_input1)
#             break
#     return user_input

# user_input1 = get_user_number()
# user_input2 = get_user_number()

# # Use function to do the math
# result = math(user_input1, user_input2)
# print(result)

# def unique_strings(lst: list) -> list:
#     def has_unique_chars(s):
#         return len(s) == len(set(s))
#     return [s for s in lst if has_unique_chars]

# lst = ["hello", "world", "abc", "deff", "unique"]
# result = unique_strings(lst)
# print(result)

from typing import List

def get_email(text: str) -> List[str]:
    text_list = text.split()
    contains_at = [word for word in text_list if '@' in word]
    contains_point = [word for word in contains_at if '.' in word.split('@', 1)[1]]
    return contains_point
text = input('Insert text with emails: ')
answer = get_email(text)
print(answer)