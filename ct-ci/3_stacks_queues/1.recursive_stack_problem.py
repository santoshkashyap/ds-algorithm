"""
    A stack can be used to implement a recursive problem iteratively.
    Example to showcase Factorial using stack
"""
from stack_using_list import StackAsList


def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)


def stack_factorial(number):
    s = StackAsList()
    while number > 0:
        s.push(number)
        number -= 1
    result = 1
    while not s.is_empty():
        result *= s.pop()
    return result


if __name__ == '__main__':
    print(f'Factorial of 5 is {factorial(5)}')
    print(f'Factorial of 5 using stack {stack_factorial(5)}')
