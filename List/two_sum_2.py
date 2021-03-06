"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:

    # approach 1
    #         start = 0
    #         end = len(numbers) - 1

    #         while start < end:
    #             pointer_addition = numbers[start] + numbers[end]
    #             if  pointer_addition == target:
    #                 return [start+1, end+1]
    #             elif target > pointer_addition:
    #                 start += 1
    #             else:
    #                 end -= 1

    # approach 2

    values = {}

    for i, num in enumerate(numbers):
        remaining = target - num
        if remaining in values:
            return [values[remaining], i + 1]
        else:
            values[num] = i + 1

    return []


if __name__ == '__main__':
    arr, target = [1, 4, 6, 7], 13
    func_call = twoSum(arr, target)
    expected_result = [3, 4]
    assert expected_result == func_call, func_call
    print(func_call)

    arr, target = [4, 6, 7, -4], 0
    func_call = twoSum(arr, target)
    expected_result = [1, 4]
    assert expected_result == func_call, func_call
    print(func_call)

    arr, target = [1, 4, 4, 3], 10
    func_call = twoSum(arr, target)
    expected_result = []
    assert expected_result == func_call, func_call
    print(func_call)

