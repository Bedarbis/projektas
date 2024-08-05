# numbers = [number for number in range(1000) if number % 6 == 0 and number != 0]
# print(numbers)

# numbers = [number for number in range(1000) if "9" in str(number)]
# print(numbers)

text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

words = text.split()

answer = [word for word in words if "e" in word]
print(len(answer))

# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

# words = text.split()

# answer = [word for word in words if len(words) > 5]
# print(len(answer))

