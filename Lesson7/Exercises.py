# class Calculator:
    
#     def add(self, x, y):
#         return x + y

#     def divide_us_please(self, x, y):
#         return x / y

#     def multiplying(self, x, y):
#         return x * y

#     def subtracting(self, x, y):
#         return x - y
    

# calculation = Calculator()

# result = calculation.add(10, 5)
# print(result)
# result = calculation.divide_us_please(10, 2)
# print(result)
# result = calculation.multiplying(5, 5)
# print(result)
# result = calculation.subtracting(5, 5)
# print(result)

# class Employee:
#     def __init__(self, name: str, lastname: str, email: str):
#         self.name = name
#         self.lastname = lastname
#         self.email = email

#     def say_name(self):
#         print(f"{self.name} {self.lastname}")
    
#     def emailas(self):
#         self.name = self.name.lower()
#         self.lastname = self.lastname.lower()
#         print(f"{self.name}.{self.lastname}{self.email}")
        
# person = Employee("Jonas", "Jonaitis", "@company.com")
# person.say_name()
# person.emailas()

# import time
# class Book:
#     def __init__(self, title: str, author: str):
#         self.title = title
#         self.author = author

#     def get_title(self):
#         print(f"Title: {self.title}")

#     def get_author(self):
#         print(f"Author: {self.author}")

# pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen (PP)")
# hamlet = Book("Hamlet", "William Shakespeare (H)")
# war_and_peace = Book("War and Peace", "Leo Tolstoy (WP)")

# print(pride_and_prejudice.title)
# print(pride_and_prejudice.author)
# pride_and_prejudice.get_title()
# pride_and_prejudice.get_author()
# print()
# time.sleep(5)
# print(hamlet.title)
# print(hamlet.author)
# hamlet.get_title()
# hamlet.get_author()
# print()
# time.sleep(5)
# print(war_and_peace.title)
# print(war_and_peace.author)
# war_and_peace.get_title()
# war_and_peace.get_author()

class Country:
    def __init__(self, name, is_big, population, area):
        self.name = name
        self.is_big = is_big
        self.population = population
        self.area = area

    is_big  self.population > 20000000 or self.area > 3000000

        

