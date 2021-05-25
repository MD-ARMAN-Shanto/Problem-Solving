# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
from typing import List
def plusOne(digits: List[int]) -> List[int]:

    if len(digits) == 0:
        # fail safe
        return digits
    else:
        # increment the number to a single integer
        number = int(''.join([str(k) for k in digits]) ) +1
        # return back a list representation
        return [int(k) for k in str(number)]


# test cases
if __name__ == '__main__':
    digits = [1, 2, 3]
    final_result = plusOne(digits)
    expected_result = [1, 2, 4]
    assert expected_result == final_result, final_result
    print(final_result)

    digits = []
    final_result = plusOne(digits)
    expected_result = []
    assert expected_result == final_result, final_result
    print(final_result)

    digits = [19]
    final_result = plusOne(digits)
    expected_result = [2, 0]
    assert expected_result == final_result, final_result
    print(final_result)

    digits = [9]
    final_result = plusOne(digits)
    expected_result = [1, 0]
    assert expected_result == final_result, final_result
    print(final_result)


