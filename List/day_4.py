# Remove duplicated element from a sorted array

from typing import List


def removeDuplicatesFromSortedArray(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]
    return nums


if __name__ == '__main__':
    nums = [1, 1, 2]
    expected_ans = [1, 2]
    final_result = removeDuplicatesFromSortedArray(nums)
    assert expected_ans == final_result, final_result
    print(final_result)

    nums = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
    expected_ans = [1, 2, 3, 4, 5, 6]
    final_result = removeDuplicatesFromSortedArray(nums)
    assert expected_ans == final_result, final_result
    print(final_result)

    nums = []
    expected_ans = []
    final_result = removeDuplicatesFromSortedArray(nums)
    assert expected_ans == final_result, final_result
    print(final_result)


def removeElement(nums: List[int], val: int) -> int:
    y = nums.count(val)
    for i in range(y):
        nums.remove(val)
    return len(nums)


nums = [1, 1, 2, 3, 4]
val = 1
final_result = removeElement(nums, val)
print(final_result)

# find out the length of common string between two string


def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    expected_ans = 2
    final_result = strStr(haystack, needle)
    assert expected_ans == final_result, final_result
    print(final_result)

    haystack = "aaaaaaaaa"
    needle = "bba"
    expected_ans = -1
    final_result = strStr(haystack, needle)
    assert expected_ans == final_result, final_result
    print(final_result)

    haystack = ""
    needle = ""
    expected_ans = 0
    final_result = strStr(haystack, needle)
    assert expected_ans == final_result, final_result
    print(final_result)
