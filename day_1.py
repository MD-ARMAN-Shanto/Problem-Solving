# # problem 1 zip using in python
#
# # solution 1 using loop with creating list of tuples
# def player_stat_fucntion(player_list, runs, wickets, catches):
#     player_stat = [(player_list[i], runs[i], wickets[i], catches[i]) for i in range(0, 10)]
#
#     print(player_stat)
#
#     return player_stat
#
#
# # solution 2 using zip make automatic list of tuple
# def player(player_list, runs, wickets, catches):
#     player_stat = list(zip(player_list, runs, wickets, catches))
#     print(player_stat)
#     return player_stat
#
#
# player_list = ['Tamim Iqbal', 'Saif Hossain', 'Nazmul Shanto', 'Mominul Haque',
#                'Mushfiqur Rahim', 'Liton Das', 'Mehedy Miraz', 'Taizul Islam',
#                'Taskin Ahmed', 'Abu Rahi', 'Shoriful Islam']
#
# runs = [158, 35, 110, 130, 75, 37, 44, 24, 12, 22, 11]
# wickets = [0, 0, 0, 0, 0, 0, 2, 1, 3, 2, 2]
# catches = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
# player(player_list, runs, wickets, catches)
#
# # problem 2 using enumerate in python
#
# import random
# from string import ascii_lowercase
#
#
# def enum_solution(given_list):
#     my_list = list(enumerate(given_list))
#     print(my_list)
#     return my_list
#
#
# given_list = random.choices(ascii_lowercase, k=6)
# enum_solution(given_list)

# problem 3 repetitive number count from a list and output as a dictionary
# solution 1

from collections import defaultdict, Counter
def repetitive_number_count(number_list):

    # freq_list = dict()
    #
    # for item in number_list:
    #     if item in freq_list:
    #         freq_list[item] += 1
    #     else:
    #         freq_list[item] = 1
    # return freq_list

    # solution 2 using defaultdict data_structure and it takes integer value and default value is 0
    # freq_list = defaultdict(int)
    # for item in number_list:
    #     freq_list[item] += 1
    # print(freq_list)
    # return freq_list

    # solution 3 using Counter Data structure for direct counting from the list
    freq_list = Counter(number_list)
    print(freq_list)
    return freq_list


if __name__ == '__main__':
    number_list = [1, 3, 5, 1, 5, 7, 7, 9, 11, 9, 11, 11, 7, 7]
    freq_num = repetitive_number_count(number_list)
    assert freq_num[1] == 2
    assert freq_num[3] == 1
    assert freq_num[5] == 2
    assert freq_num[7] == 4
    assert freq_num[9] == 2
    assert freq_num[11] == 3
    assert freq_num[12] == 0
