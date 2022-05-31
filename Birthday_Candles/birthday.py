def birthday(s, d, m):
    i, j = 0, 0
    count, add = 0, 0

    while j < len(s):
        add += s[j]

        if j - i + 1 < m:
            j += 1

        elif j - i + 1 == m:
            if add == d:
                count += 1
            add -= s[i]
            i += 1
            j += 1

    return count


if __name__ == "__main__":
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2
    expected_result = 2
    output = birthday(s, d, m)
    assert expected_result == output, output
    print(output)