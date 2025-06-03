list_players_cards = input()

# parse string
list_players_cards_raw_old = list_players_cards.split(" ")

count_a_team = 11
count_b_team = 11
# data normalization - version 1
# list_players_cards_raw = []
# for item in list_players_cards_raw_old:
#     if item not in list_players_cards_raw:
#         list_players_cards_raw.append(item)

# data normalization - version 2 with set
list_players_cards_raw = list(set(list_players_cards_raw_old))
is_game_stopped = False

for player_cards in list_players_cards_raw:
    if list_players_cards_raw.count(player_cards) > 1:
        continue
    team,player_number = player_cards.split("-")
    if team == "A":
        count_a_team -= 1
        if count_a_team < 7:
            is_game_stopped = True
            break
    elif team == "B":
        count_b_team -= 1
        if count_b_team < 7:
            is_game_stopped = True
            break

print(f"Team A - {count_a_team}; Team B - {count_b_team}")
if is_game_stopped:
    print("Game was terminated")

