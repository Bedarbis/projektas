# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)

# squares = [number * number for number in range(10)]
# print(squares)

# squares = [number * number for number in range(10) if number != 5]
# print(squares)

# squares = [number * number for number in range(10) if number % 2 == 0]
# print(squares)

# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A")])

# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A") or "e" in name])

# squares = {i: i * i for i in range(10)}
# print(squares)

# values = ["a", "b", "c"]
# index = 0
# for value in values:
#     print(value, value)
#     index += 1

# values = ["a", "b", "c"]
# for index, value in enumerate(values):
#     print(count, value)

import math
area = 5 * 5 * math.pi

import math
print (math.sqrt(9))