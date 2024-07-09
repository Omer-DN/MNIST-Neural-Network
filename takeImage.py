def myrevers(n: int) -> int:
    n = str(n)
    myRevers = int(n[::-1])
    return myRevers


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_digits(n: int) -> int:
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def reverse_string_words(s: str) -> str:
    word = s.split(" ")
    new_word = []
    for i in range(len(word)):
        new_word.append(word[i][::-1])
    return " ".join(new_word)


def sum_numbers(numbers: int) -> int:
    return sum(numbers)


from functools import reduce


def multiply_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)


def double_numbers(numbers):
    return list(map(lambda x: x * 2, numbers))


def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def sort_positive_negative(numbers):
    posNum = sorted(list(filter(lambda x: x >= 0, numbers)))
    negNum = sorted(list(filter(lambda x: x < 0, numbers)))
    return negNum + posNum

def uppercase_strings(strings):
    return (list(map(str.upper, strings)))


def multiply_numbers(numbers):
    return reduce(lambda x,y:x*y,numbers,1 )

# print(multiply_numbers([1, 2, 3, 4,5]))     # פלט צפוי: 24

# print(uppercase_strings(["hello", "world"]))     # פלט צפוי: ['HELLO', 'WORLD']

# print(sort_positive_negative([1, -2, 3, -4, 5, -6]))  # פלט צפוי: [1, 3, 5, -6, -4, -2]

# print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # פלט צפוי: [2, 4, 6]

# print(double_numbers([1, 2, 3, 4, 5]))   # פלט צפוי: [2, 4, 6, 8, 10]

# print(multiply_numbers([1, 2, 3, 4, 5]))   # פלט צפוי: 120

# print(sum_numbers([10]))

# print(reverse_string_words("python is awesome"))

# print (sum_of_digits(123))

# print(is_prime(3))

# print(myRevers(12345))
