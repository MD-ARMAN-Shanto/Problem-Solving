"""
Approach: linearSearch and two pointer
Status: Accepted
131 / 131 test cases passed.
Runtime: 32 ms
Memory Usage: 15.6 MB
Problem link: https://leetcode.com/problems/remove-element/
Time complexity: O(n)
space complexity: O(1)
"""

from typing import List

# linearSearch
def removeElement(nums: List[int], val: int) -> int:

    y = nums.count(val)
    for i in range(y):
        nums.remove(val)
    return len(nums)


# two pointer approach
def removeElement1(nums: List[int], val: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        if nums[start] == val:
            nums[start] = nums[end]
            nums[end] = nums[start]
            end -= 1
        else:
            start += 1
    return start


if __name__ == '__main__':
    nums, val = [3, 2, 2, 3], 3
    func_call = removeElement(nums, val)
    expected_result = 2
    assert expected_result == func_call, func_call
    print(func_call)
