"""
reverse a stack using recursion

given input : [1,2,3,4,5]
expected output : [5,4,3,2,1]
"""
from typing import List


def reverseStack(numbers: List[int]) -> List[int]:

    # base case always return value
    if len(numbers) == 1:
        return numbers

    # Hypothesis, smaller the input list
    temp = numbers[-1]
    numbers.pop()

    reverseStack(numbers)

    # induction step where temp value insert into the stack
    insertIntoStack(numbers, temp)

    return numbers


def insertIntoStack(numbers: List[int], number: int) -> List[int]:

    # base case always return value
    if len(numbers) == 0:
        numbers.append(number)
        return numbers

    # Hypothesis, smaller the input
    temp = numbers[-1]
    numbers.pop()

    insertIntoStack(numbers, number)

    numbers.append(temp)

    return numbers


if __name__ == '__main__':
    stack = [1, 2, 3, 4, 5]
    func_call = reverseStack(stack)
    expected_result = [5, 4, 3, 2, 1]
    assert expected_result == func_call, func_call
    print(func_call)

    stack = [6, 4, 9, 3, 8, 1]
    func_call = reverseStack(stack)
    expected_result = [1, 8, 3, 9, 4, 6]
    assert expected_result == func_call, func_call
    print(func_call)