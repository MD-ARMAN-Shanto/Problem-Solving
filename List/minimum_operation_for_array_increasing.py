"""
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

Example 1:

Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].
"""
from typing import List


def minOperations(nums: List[int]) -> int:
    count = 0

    if len(nums) == 1:
        return 0

    for num in range(1, len(nums)):
        fn = nums[num - 1]
        sn = nums[num]

        if sn <= fn:
            diff = fn - sn
            sn += diff + 1
            count += diff + 1
            nums[num] = sn

        else:
            continue

    return count


if __name__ == '__main__':
    arr = [1, 5, 2, 4, 1]
    fc = minOperations(arr)
    expected_result = 14
    assert expected_result == fc, fc
    print(fc)