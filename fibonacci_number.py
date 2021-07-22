# fibonacci Number problem set, given a number of term of series,
# and we have to find out the sum number using fibonacci series.


# we will try to solve it in a O(n) time complexity with O(1) space complexity

import time
from typing import List
from functools import lru_cache

start_time = time.time()


def fibonacci_series(n: int) -> int:
    # error return
    if n < 0:
        return 0

    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # initialize the base case logic
        fib1 = 0
        fib2 = 1
        i = 2
        while i <= n:
            temp = fib1 + fib2
            fib1 = fib2
            fib2 = temp
            i += 1

    return temp


if __name__ == '__main__':
    number = 3
    function__call = fibonacci_series(number)
    expected_result = 2
    assert expected_result == function__call, function__call
    print(function__call)

    number = -5
    function__call = fibonacci_series(number)
    expected_result = 0
    assert expected_result == function__call, function__call
    print(function__call)

    number = 10
    function__call = fibonacci_series(number)
    expected_result = 55
    assert expected_result == function__call, function__call
    print(function__call)

    number = 33
    function__call = fibonacci_series(number)
    expected_result = 3524578
    assert expected_result == function__call, function__call
    print(function__call)

print("--- %s miliseconds ---" % ((time.time() - start_time) * 1000))

# another approach to solve fibonacci_series in a recursive process
# in recursive way the time complexity of fibonacci_series will be O(2^n) and space complexity will be O(n)


def fibonacci_recursive(n: int) -> int:

    if n <= 1:
        return n

    return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))


if __name__ == '__main__':
    number = 3
    function__call = fibonacci_recursive(number)
    expected_result = 2
    assert expected_result == function__call, function__call
    print(function__call)

    number = -5
    function__call = fibonacci_recursive(number)
    expected_result = -5
    assert expected_result == function__call, function__call
    print(function__call)

    number = 10
    function__call = fibonacci_recursive(number)
    expected_result = 55
    assert expected_result == function__call, function__call
    print(function__call)

    number = 33
    function__call = fibonacci_recursive(number)
    expected_result = 3524578
    assert expected_result == function__call, function__call
    print(function__call)

print("--- %s miliseconds ---" % ((time.time() - start_time) * 1000))


# another solution for fibonacci series is recursive with memoization
# fibonacci with memoization is help to reduce the time complexity of the program
# time complexity of fibonacci with memoization will be O(n^2)


@lru_cache
def fibonacci_recursive_memoization(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci_recursive_memoization(n-1) + fibonacci_recursive_memoization(n-2)


if __name__ == '__main__':
    number = 3
    function__call = fibonacci_recursive_memoization(number, )
    expected_result = 2
    assert expected_result == function__call, function__call
    print(function__call)

    number = -5
    function__call = fibonacci_recursive_memoization(number)
    expected_result = -5
    assert expected_result == function__call, function__call
    print(function__call)

    number = 10
    function__call = fibonacci_recursive_memoization(number)
    expected_result = 55
    assert expected_result == function__call, function__call
    print(function__call)

    number = 33
    function__call = fibonacci_recursive_memoization(number)
    expected_result = 3524578
    assert expected_result == function__call, function__call
    print(function__call)

print("--- %s miliseconds ---" % ((time.time() - start_time) * 1000))

