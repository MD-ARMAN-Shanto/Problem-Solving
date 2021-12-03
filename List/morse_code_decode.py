"""
programmed by MD. Arman Hossain
"""
from typing import List


def uniqueMorseRepresentations(words: List[str]) -> int:
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    res = {}
    a = ''
    count, total = 1, 0

    for word in words:
        for ch in word:
            a += morse_code[ord(ch) - 97]

        if a not in res:
            res[a] = count
        a = ''

    for value in res.values():
        total += value

    return total


if __name__ == '__main__':
    li = ["gin", "zen", "gig", "msg"]
    fc = uniqueMorseRepresentations(li)
    expected_result = 2
    assert expected_result == fc, fc
    print(fc)

    li = ["a"]
    fc = uniqueMorseRepresentations(li)
    expected_result = 1
    assert expected_result == fc, fc
    print(fc)

    li = []
    fc = uniqueMorseRepresentations(li)
    expected_result = 0
    assert expected_result == fc, fc
    print(fc)
