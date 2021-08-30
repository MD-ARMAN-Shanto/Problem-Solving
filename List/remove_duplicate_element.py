"""
Approach: linearSearch
Status: Accepted
131 / 131 test cases passed.
Runtime: 96 ms
Memory Usage: 15.6 MB
Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Time complexity: O(n)
space complexity: O(1)
"""

from typing import List


def removeDuplicates(nums: List[int]) -> any:
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]
    return nums


if __name__ == '__main__':
    nums = [1, 1, 2]
    func_call = removeDuplicates(nums)
    expected_result = [1, 2]
    assert expected_result == func_call, func_call
    print(func_call)

    nums = [0, 0, 0, 1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7]
    func_call = removeDuplicates(nums)
    expected_result = [0, 1, 2, 3, 4, 5, 6, 7]
    assert expected_result == func_call, func_call
    print(func_call)