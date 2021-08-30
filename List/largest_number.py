# find out the largest numbr from an array

from typing import List


def largest_number(arr: List[int]) -> int:
    largest = 0

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest


if __name__ == '__main__':
    arr_num = [2, 4, 20, 33, 15, 17, 50, 32, 1, 9, 13]
    final_result = largest_number(arr_num)
    print(final_result)
