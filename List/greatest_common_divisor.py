""" GCD Eucledian Algorithm

       general equation
       step 1: bigest_number = smallest_number * nearer_times + remainder
       step 2: smallest_number = remainder * nearer_times + new_remainder
       step 3: remainder = new_remainder * nearer_times + n_new_remainder
       go until the last past will be zero then the previous number of the remainder would be the GCD of         the two number


       GCD(10, 45)

       45 = 10 * 4 + 5 --> GCD
       10 = 5 * 2 + 0

"""
from typing import List


def gcd(nums: List[int]) -> int:

    min_value = min(nums)
    max_value = max(nums)

    while min_value < max_value:
        remainder = max_value % min_value

        if remainder == 0:
            return min_value

        max_value = min_value
        min_value = remainder

    return min_value


if __name__ == '__main__':
    nums = [2, 5, 6, 9, 10]
    fc = gcd(nums)
    expected_result = 2
    assert expected_result == fc, fc
    print(fc)

    nums = [7, 5, 6, 8, 3]
    fc = gcd(nums)
    expected_result = 1
    assert expected_result == fc, fc
    print(fc)

    nums = [3, 3]
    fc = gcd(nums)
    expected_result = 3
    assert expected_result == fc, fc
    print(fc)

