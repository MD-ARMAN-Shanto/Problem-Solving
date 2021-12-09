"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the
secondary diagonal that are not part of the primary diagonal.

Ex 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Input: mat = [[5]]
Output: 5

"""

from typing import List


def matrixDiagonalSum(mat: List[List[int]]) -> int:

    primary_diagonal = 0
    secondary_diagonal = 0

    # first approach, time complexity O(n^2)
    # for index in range(len(mat)):
    #     for element_position in range(len(mat[index])):
    #         if index == element_position:
    #             primary_diagonal += mat[index][element_position]
    #
    #         if index + element_position == len(mat) - 1:
    #             if index != element_position:
    #                 secondary_diagonal += mat[index][element_position]
    # return primary_diagonal+secondary_diagonal

    # second approach, time complexity O(n^2)
    n = len(mat)

    for index in range(len(mat)):
        primary_diagonal += mat[index][index]

        if index + index != n - 1:
            secondary_diagonal += mat[index][n - index - 1]

    return primary_diagonal +secondary_diagonal


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    fc = matrixDiagonalSum(mat)
    expected_result = 25
    assert expected_result == fc, fc
    print(fc)

