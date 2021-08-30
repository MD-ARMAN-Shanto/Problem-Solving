# linear search algorithm implemantation on python
# time complexity O(n) and space complexity O(1)

from typing import List


def linearSearch(numbers: List[int], searchValue) -> int:

    for i in range(len(numbers)):
        if numbers[i] == searchValue:
            return numbers[i]

    return -1


# test cases
if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9]
    searchValue = 9
    expected_result = 9
    final_result = linearSearch(numbers, searchValue)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [1, 3, 5, 7, 9]
    searchValue = 10
    final_result = linearSearch(numbers, searchValue)
    expected_result = -1
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [1, 3, 5, 7, 9]
    searchValue = 1
    final_result = linearSearch(numbers, searchValue)
    expected_result = 1
    assert expected_result == final_result, final_result
    print(final_result)


