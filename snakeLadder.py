import random

tot_players = int(input("Enter Total Players:"))
scores = [0] * tot_players

tot_scores = []


curr_player = 1
while True:
    print("Player",curr_player,"Play your turn")
    print("Press Enter to roll a Die")
    input()
    ls = [1,2,3,4,5,6]
    rolled = random.choice(ls)
    print("You rolled:",rolled)
    
    scores[curr_player - 1] = scores[curr_player - 1 ] + rolled
    print("Total Scores:",scores[curr_player - 1])
    curr_player = curr_player + 1

    if curr_player > tot_players:
        curr_player = 1
    

