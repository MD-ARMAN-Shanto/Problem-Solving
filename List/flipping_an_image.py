"""
programmed by MD. Arman Hossain
"""
from typing import List


def flipAndInvertImage(images: List[List[int]]) -> List[List[int]]:
    i_list = []
    result = []

    for image in images:
        res = image[::-1]
        for num in res:
            if num == 0:
                num = 1
            else:
                num = 0
            i_list.append(num)

        result.append(i_list)
        i_list = []

    return result


