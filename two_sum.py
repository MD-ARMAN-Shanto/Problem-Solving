# find out the at least one pair/two integer numbers/position of the two integer numbers from an array which number
# of sum equals to the target numbers if target number is not found in the array return an empty array

# solution 1 : brute force

from typing import List


def two_sum(arr: List[int], target: int) -> List[int]:

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]
    return []

# time complexity O(n * n) = O(n^2)
# space complexity O(1)


if __name__ == '__main__':
    arr, target = [1, 4, 6, 7], 13
    func_call = two_sum(arr, target)
    expected_result = [6, 7]
    assert expected_result == func_call, func_call
    print(func_call)

    arr, target = [4, 6, 7, -4], 0
    func_call = two_sum(arr, target)
    expected_result = [4, -4]
    assert expected_result == func_call, func_call
    print(func_call)

    arr, target = [1, 4, 4, 3], 10
    func_call = two_sum(arr, target)
    expected_result = []
    assert expected_result == func_call, func_call
    print(func_call)


# adding two sum with better approach

# two pointer approach

#Todo
# step 1: first sort the given array
# step 2: take start and end(upto it's length) position from the array
# step 3: take a while loop until start < end
# step 4: if arr[start] + arr[end] == target, return value
# step 5: if sum > target then end -+ 1 else sum < target then  start +=1

def two_sum_pointer(arr: List[int], target: int) -> List[int]:

    arr.sort()

    start = 0
    end = len(arr) - 1

    while start < end:
        sum: int = arr[start] + arr[end]
        if sum == target:
            return [arr[start], arr[end]]

        if sum > target:
            end -= 1
        elif sum < target:
            start += 1
    return []


if __name__ == '__main__':
    arr, target = [1, 4, 6, 7], 13
    func_call = two_sum_pointer(arr, target)
    expected_result = [6, 7]
    assert expected_result == func_call, func_call
    print(func_call)

    arr, target = [4, 6, 7, -4], 0
    func_call = two_sum_pointer(arr, target)
    expected_result = [-4, 4]
    assert expected_result == func_call, func_call
    print(func_call)

    arr, target = [1, 4, 4, 3], 10
    func_call = two_sum_pointer(arr, target)
    expected_result = []
    assert expected_result == func_call, func_call
    print(func_call)




