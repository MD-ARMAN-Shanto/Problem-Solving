"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
from typing import List


def moveZeroes(nums: List[int]) -> list[int]:
    """
    Do not return anything, modify nums in-place instead.
    """

    i = 0

    for num in range(len(nums)):

        if nums[num] != 0:
            nums[i], nums[num] = nums[num], nums[i]
            i += 1

    return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    func_call = moveZeroes(nums)
    expected_result = [1, 3, 12, 0, 0]
    assert expected_result == func_call, func_call
    print(func_call)

    nums = [0, 1, 0, 3, 12, 0, 9, 34, 4, 0]
    func_call = moveZeroes(nums)
    expected_result = [1, 3, 12, 9, 34, 4, 0, 0, 0, 0]
    assert expected_result == func_call, func_call
    print(func_call)