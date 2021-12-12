"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from typing import List


def majorityElement(nums: List[int]) -> int:

    res = {}

    for num in range(len(nums)):
        if nums[num] not in res:
            res[nums[num]] = 1
        else:
            res[nums[num]] += 1

    return max(res, key=res.get)