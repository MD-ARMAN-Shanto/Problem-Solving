# find out the highest scores and lowest score record count for any players scores list

# score_list = [2, 4, 6, 1, 8, 10]
# highest score = 4
# lowest score = 1
# list of score count = [4, 1]

def score_records(score_list):

    highest_score = score_list[0]
    lowest_score = score_list[0]

    highest_score_count = 0
    lowest_score_count = 0

    for i in range(len(score_list)):
        if highest_score < score_list[i]:
            highest_score = score_list[i]
            highest_score_count += 1
        elif score_list[i] < lowest_score:
            lowest_score = score_list[i]
            lowest_score_count += 1
    return [highest_score_count, lowest_score_count]


if __name__ == '__main__':
    score_list = [2, 4, 6, 1, 8, 10]
    expected_ans = [4, 1]
    final_result = score_records(score_list)
    assert expected_ans == final_result, final_result
    print(final_result)

    score_list = [5, 7, 9, 4, 3, 2, 1, 15]
    expected_ans = [3, 4]
    final_result = score_records(score_list)
    assert expected_ans == final_result, final_result
    print(final_result)

    score_list = [500, 550, 570, 590, 300, 250, 200, 150, 750, 800, 100, 50]
    expected_ans = [5, 6]
    final_result = score_records(score_list)
    assert expected_ans == final_result, final_result
    print(final_result)