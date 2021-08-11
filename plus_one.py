"""
Approach: linearSearch
Status: Accepted
131 / 131 test cases passed.
Runtime: 96 ms
Memory Usage: 15.6 MB
Problem link: https://leetcode.com/problems/plus-one/
Time complexity: O(n)
space complexity: O(1)
"""
from typing import List


def plusOne(nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return nums

    else:
        result = int(''.join([str(k) for k in nums])) + 1
        return [int(k) for k in str(result)]


if __name__ == '__main__':
    nums = [1, 2, 3]
    func_call = plusOne(nums)
    expected_result = [1, 2, 4]
    assert expected_result == func_call, func_call
    print(func_call)

    nums = [4, 3, 2, 1]
    func_call = plusOne(nums)
    expected_result = [4, 3, 2, 2]
    assert expected_result == func_call, func_call
    print(func_call)

    nums = [0]
    func_call = plusOne(nums)
    expected_result = [1]
    assert expected_result == func_call, func_call
    print(func_call)
