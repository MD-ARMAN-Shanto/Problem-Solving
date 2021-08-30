# find out the single number from an array with linear time complexity O(n).

from typing import List


def single_number(nums: List[int]) -> int:
    """counts = {}

    for n in nums:
        if n not in counts:
            counts[n] = 1
        else:
            del counts[n]
    return list(counts.keys())[0]"""

    a = 0
    for i in nums:
        a ^= i
    return a


if __name__ == '__main__':
    nums = [2, 3, 4, 3, 2]
    func_call = single_number(nums)
    expected_answer = 4
    assert expected_answer == func_call, func_call
    print(expected_answer)
