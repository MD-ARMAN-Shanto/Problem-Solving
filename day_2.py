# problem is to fine out the prieme divisible number of any Number

from math import sqrt


def prime_divisible_value(number):
    factors_list = []

    while number % 2 == 0:
        number //= 2
        factors_list.append(2)

    sqrt_num = int(sqrt(number))

    for i in range(3, sqrt_num, 2):
        while number % i == 0:
            number //= i
            factors_list.append(i)

    if number > 1:
        factors_list.append(number)
    return factors_list


if __name__ == '__main__':
    number = 4
    expected_ans = [2, 2]
    factors = prime_divisible_value(number)
    assert expected_ans == factors, factors
    print(factors)

    number = 10
    expected_ans = [2, 5]
    factors = prime_divisible_value(number)
    assert expected_ans == factors, factors
    print(factors)

    number = 27
    expected_ans = [3, 3, 3]
    factors = prime_divisible_value(number)
    assert expected_ans == factors, factors
    print(factors)

    number = 101
    expected_ans = [101]
    factors = prime_divisible_value(number)
    assert expected_ans == factors, factors
    print(factors)

    number = 1
    expected_ans = []
    factors = prime_divisible_value(number)
    assert expected_ans == factors, factors
    print(factors)