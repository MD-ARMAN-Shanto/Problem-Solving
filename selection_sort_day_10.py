# selection sort algorithm asc order small to max
# time complexity O(n^2) time complexity O(1)

from typing import List


def selectionSortSmallToMax(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        index_min = i

        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[index_min]:
                index_min = j

        if index_min != i:
            temp = numbers[i]
            numbers[i] = numbers[index_min]
            numbers[index_min] = temp

    return numbers


# test cases

if __name__ == '__main__':
    numbers = [5, 3, 4, 7]
    expected_result = [3, 4, 5, 7]
    final_result = selectionSortSmallToMax(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [50, 30, 45, 73]
    expected_result = [30, 45, 50, 73]
    final_result = selectionSortSmallToMax(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = []
    expected_result = []
    final_result = selectionSortSmallToMax(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [-2, -5, 3, 1]
    expected_result = [-5, -2, 1, 3]
    final_result = selectionSortSmallToMax(numbers)
    assert expected_result == final_result, final_result
    print(final_result)


# selection sort desc order max to small


def selectionSortMaxToSmall(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        index_min = i

        for j in range(i+1, len(numbers)):
            if numbers[j] > numbers[index_min]:
                index_min = j

        if index_min != i:
            temp = numbers[i]
            numbers[i] = numbers[index_min]
            numbers[index_min] = temp

    return numbers


if __name__ == '__main__':
    numbers = [3, 5, 4, 7]
    expected_result = [7, 5, 4, 3]
    final_result = selectionSortMaxToSmall(numbers)
    assert expected_result == final_result, final_result
    print(final_result)