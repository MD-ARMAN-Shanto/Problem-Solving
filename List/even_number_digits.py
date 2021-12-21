"""
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.
"""
from math import log10, floor
from typing import List


def findNumbers(nums: List[int]) -> int:

    # approach 1
    #         res = []
    #         target = 1

    #         for num in nums:
    #             count = 0

    #             while(num != 0):
    #                 num = num // 10
    #                 count += 1
    #             if count % 2 == 0:
    #                 res.append(target)
    #                 target+=1

    #         return len(res)

    # approach 2
    arr = []
    count = 0
    for num in nums:
        res = floor(log10(num) + 1)
        if res % 2 == 0:
            arr.append(count)
            count += 1
    return len(arr)


if __name__ == '__main__':
    nums = [12, 345, 2, 6, 7896]
    func_call = findNumbers(nums)
    expected_result = 2
    assert expected_result == func_call, func_call
    print(func_call)

    nums = [555, 901, 482, 1771]
    func_call = findNumbers(nums)
    expected_result = 1
    assert expected_result == func_call, func_call
    print(func_call)
