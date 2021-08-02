"""
Approach: Two Pointer
Status: Accepted
131 / 131 test cases passed.
Runtime: 120 ms
Memory Usage: 14.3 MB
Problem link: https://leetcode.com/problems/3sum-closest
Time complexity: O(n^2)
space complexity: O(1)
"""

from typing import List


def three_sum(nums: List[int], target: int) -> int:
    nums.sort()
    result = nums[0] + nums[1] + nums[len(nums) - 1]  # for comparison

    for i in range(len(nums)-1):
        left = i + 1
        right = len(nums)-1
        while left < right:
            current = nums[i] + nums[left] + nums[right]

            if current == target:
                return target
            elif abs(target-current) < abs(target-result):
                result = current
            elif current < target:
                left += 1
            elif current > target:
                right -= 1
    return result


if __name__ == '__main__':
    nums, target = [-4, -1, 1, 2], 1
    function = three_sum(nums, target)
    expected_result = 2
    assert expected_result == function, function
    print(function)