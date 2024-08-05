# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
    
#     def travel(self):
#         print(f"{self.name} is walking...")
    
#     def say_hello(self) -> None:
#         print(f"{self.name} shouts Hellooo!")
    
#     def increment_year(self) -> None:
#         self.age = self.age + 1


# person1 = Person("Tom", 40)
# person2 = Person("Petras", 69)
# person1.increment_year()

# print(person1.age)
# print(person1.say_hello())

# print(person2.age)
# print(person2.say_hello())


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def travel(self):
        print(f"{self.name} is walking...")

    def say_hello(self) -> None:
        print(f"{self.name} says Hello!")

class Driver(Person):
    def travel(self):
        print(f"{self.name} is driving a car... much faster than walking")

person1 = Person("Tom", 40)
person2 = Driver("Petras", 69)

person1.say_hello()
person2.say_hello()
person1.travel()
person2.travel()
