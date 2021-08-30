# insertion sorting
# time complexity O(n^2) and space complexity O(1)

from typing import List


def insertionSort(numbers: List[int]) -> List[int]:
    for i in range(1, len(numbers)):
        item = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > item:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j+1] = item

    return numbers


# test cases
if __name__ == '__main__':
    numbers = [5, 3, 4, 7]
    expected_result = [3, 4, 5, 7]
    final_result = insertionSort(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [50, 30, 45, 73]
    expected_result = [30, 45, 50, 73]
    final_result = insertionSort(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = []
    expected_result = []
    final_result = insertionSort(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [-2, -5, 3, 1]
    expected_result = [-5, -2, 1, 3]
    final_result = insertionSort(numbers)
    assert expected_result == final_result, final_result
    print(final_result)
