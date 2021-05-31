# binary search algorithm
# time complexity O(nlogn) and space complexity )(n)

from typing import List


def binarySearch(numbers: List[int], value) -> int:
    if len(numbers) == 0:
        return -1

    n = len(numbers)
    left_val = 0
    right_val = n - 1

    while left_val <= right_val:
        mid = int((left_val + right_val) / 2)
        print(mid)

        if numbers[mid] == value:
            return mid

        if numbers[mid] < value:
            left_val = mid + 1
            print('left_val', left_val)
        else:
            right_val = mid - 1
            print('right_val', right_val)

    return -1


# test cases
if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9]
    searchValue = 9
    expected_result = 4
    final_result = binarySearch(numbers, searchValue)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [1, 3, 5, 7, 9]
    searchValue = 10
    expected_result = -1
    final_result = binarySearch(numbers, searchValue)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [1, 3, 5, 7, 9]
    searchValue = 3
    expected_result = 1
    final_result = binarySearch(numbers, searchValue)
    assert expected_result == final_result, final_result
    print(final_result)
