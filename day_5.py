# find out the insert point of any integer value

from typing import List


def findInsert(nums: List[int], target: int) -> int:
    if target not in nums:
        nums.append(target)

    return sorted(nums).index(target)


if __name__ == '__main__':
    nums = [1, 3, 5, 7]
    target = 9
    expected_ans = 4  # index number
    final_result = findInsert(nums, target)
    assert expected_ans == final_result, final_result
    print(final_result)

    nums = [1]
    target = 1
    expected_ans = 0
    final_result = findInsert(nums, target)
    assert expected_ans == final_result, final_result
    print(final_result)
