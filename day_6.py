# find out the maximum subarray from a list

from typing import List


def maximumSubArray(numbers: List[int]) -> int:
    # take the first value as higest number of subarray
    max_so_far = numbers[0]
    max_ending_here = 0  # intial sum count

    for i in range(len(numbers)):
        max_ending_here += numbers[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected_result = 6
    final_result = maximumSubArray(nums)
    assert expected_result == final_result, final_result
    print(final_result)
