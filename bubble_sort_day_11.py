# bubble sorting small to max asc order
# time complexity O(n^2) and space complexity O(1)

from typing import List


def bubbleSortSmallToMax(numbers:List[int]) -> List[int]:

    for i in range(len(numbers)):
        for j in range(0, len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


# test cases

if __name__ == '__main__':
    numbers = [5, 3, 4, 7]
    expected_result = [3, 4, 5, 7]
    final_result = bubbleSortSmallToMax(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [50, 30, 45, 73]
    expected_result = [30, 45, 50, 73]
    final_result = bubbleSortSmallToMax(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = []
    expected_result = []
    final_result = bubbleSortSmallToMax(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [-2, -5, 3, 1]
    expected_result = [-5, -2, 1, 3]
    final_result = bubbleSortSmallToMax(numbers)
    assert expected_result == final_result, final_result
    print(final_result)


# bubble sorting array max to small desc order


def bubbleSortMaxToSmall(numbers:List[int]) -> List[int]:

    for i in range(len(numbers)):
        for j in range(0, len(numbers)-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


# test cases

if __name__ == '__main__':
    numbers = [5, 3, 4, 7]
    expected_result = [7, 5, 4, 3]
    final_result = bubbleSortMaxToSmall(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [50, 30, 45, 73]
    expected_result = [73, 50, 45, 30]
    final_result = bubbleSortMaxToSmall(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = []
    expected_result = []
    final_result = bubbleSortMaxToSmall(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

    numbers = [-2, -5, 3, 1]
    expected_result = [3, 1, -2, -5]
    final_result = bubbleSortMaxToSmall(numbers)
    assert expected_result == final_result, final_result
    print(final_result)

