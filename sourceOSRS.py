import random

import runescapeapi as rs
import OSRSwords

OSRS_player_list = ['lemongrab_fe', '7_45_PM', 'dietsheep', "Zezima", "CraniumMash"]


def new_chosen_player(player: str) -> dict:
    player_info_dict = {}
    print(player)
    hiscor = rs.Highscores(player, 'hiscore_oldschool_ironman')
    # hs_dict = rs.Highscores(player, 'hiscore_oldschool_ironman').skills
    player_info_dict[player] = hiscor.total['xp']
    for skill in hiscor.skills:
        player_info_dict[skill['name']] = [skill['level'], skill['xp']]
    return player_info_dict


def create_IDUTC() -> (str, str):
    user_string = random.choice(OSRS_player_list)
    player_dict = new_chosen_player(user_string)
    # print(player_dict)
    useID = user_string
    useUTC = player_dict[useID] % 1000000000000
    while useUTC < 1000000000:
        useUTC *= 10
        useUTC += 3
    return useID, useUTC
