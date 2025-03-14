# Task 1
def power_numbers(*args: int):
    """
    функция, которая принимает N целых чисел и возвращает список квадратов этих чисел
    """
    return [pow(x, 2) for x in args]


exp_numbers = power_numbers(1, 2, 5, 7, 8, 9, 125)
print(exp_numbers)

# Task 2

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    """
    функция, которая на вход принимает целое число,
    и проверяет простое оно или нет
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    """
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))
    else:
        raise ValueError("Не корректный тип данных. Введите ODD, EVEN или PRIME")


print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], EVEN))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ODD))
print(filter_numbers([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 19, 20], PRIME))
