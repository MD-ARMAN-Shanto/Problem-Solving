def search(txt, pat):
    # code here
    i, j = 0, 0

    d = {}

    for p in pat:
        d[p] = d.get(p, 0) + 1

    count = len(d)

    ans = 0

    while j < len(txt):

        if txt[j] in d:
            d[txt[j]] -= 1
            if d[txt[j]] == 0:
                count -= 1

        if j - i + 1 < len(pat):
            j += 1

        elif j - i + 1 == len(pat):
            if count == 0:
                ans += 1
            if txt[i] in d:
                d[txt[i]] += 1
                if d[txt[i]] == 1:
                    count += 1

            i += 1
            j += 1

    return ans


if __name__ == '__main__':
    haystack = "foradsdifhuasd"
    needle = "for"
    expected_ans = 1
    final_result = search(haystack, needle)
    assert expected_ans == final_result, final_result
    print(final_result)

