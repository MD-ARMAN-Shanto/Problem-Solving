"""
Approach: linearSearch
Status: Accepted
131 / 131 test cases passed.
Runtime: 96 ms
Memory Usage: 15.6 MB
Problem link: https://leetcode.com/problems/maximum-subarray/
Time complexity: O(n)
space complexity: O(1)
"""

from typing import List


def maximumSubArray(nums: List[int]) -> int:

    max_so_far = nums[0]
    max_ending_here = 0

    for i in range(len(nums)):
        max_ending_here = max_ending_here + nums[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    func_call = maximumSubArray(nums)
    expected_result = 6
    assert expected_result == func_call, func_call
    print(func_call)

    nums = [5, 4, -1, 7, 8]
    func_call = maximumSubArray(nums)
    expected_result = 23
    assert expected_result == func_call, func_call
    print(func_call)

    nums = [1]
    func_call = maximumSubArray(nums)
    expected_result = 1
    assert expected_result == func_call, func_call
    print(func_call)



