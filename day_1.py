
# solution 1 using loop with creating list of tuples
def player_stat_fucntion(player_list, runs, wickets, catches):

    player_stat = [(player_list[i], runs[i], wickets[i], catches[i]) for i in range(0, 10)]

    print(player_stat)

    return player_stat


# solution 2 using zip make automatic list of tuple
def player(player_list, runs, wickets, catches):

    player_stat = list(zip(player_list, runs, wickets, catches))
    print(player_stat)
    return player_stat


player_list = ['Tamim Iqbal', 'Saif Hossain', 'Nazmul Shanto', 'Mominul Haque',
               'Mushfiqur Rahim', 'Liton Das', 'Mehedy Miraz', 'Taizul Islam',
               'Taskin Ahmed', 'Abu Rahi', 'Shoriful Islam']

runs = [158, 35, 110, 130, 75, 37, 44, 24, 12, 22, 11]
wickets = [0, 0, 0, 0, 0, 0, 2, 1, 3, 2, 2]
catches = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
player(player_list, runs, wickets, catches)