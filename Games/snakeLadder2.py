import random

player1 = input("Enter player-1 Name:")
player2 = input("Enter player-2 Name:")

player1_score = 0
player2_score = 0
ls = [1,2,3,4,5,6]

i=1
while True:
    print()
    print(player1,"Its your turn roll a die press Enter")
    input()
    player1_Rolled = random.randint(1,6)
    print(player1,"You rolled :",player1_Rolled)
    if player1_score + player1_Rolled <= 100:
        player1_score = player1_score + player1_Rolled
    else:
        player1_score = player1_score

    print()
    print(player2,"Its your turn roll a die press Enter")
    input()
    player2_Rolled = random.randrange(1,6)
    print(player2,"You rolled:",player2_Rolled)

    if player2_score + player2_Rolled <= 100:
        player2_score = player2_score + player2_Rolled
    else:
        player2_score = player2_score

    if player1_score == 1 : 
        print("WOW you got a Ladder🙌")
        player1_score = 38

    if player1_score == 4 : 
        print("WOW you got a Ladder🙌")
        player1_score = 14

    if player1_score == 9 : 
        print("WOW you got a Ladder🙌")
        player1_score = 31

    if player1_score == 21 : 
        print("WOW you got a Ladder🙌")
        player1_score = 42

    if player1_score == 28 : 
        print("WOW you got a Super-Ladder🙌")
        player1_score = 84 
    
    if player1_score == 51 : 
        print("WOW you got a Ladder🙌")
        player1_score = 67

    if player1_score == 72 : 
        print("WOW you got a Ladder🙌")
        player1_score = 91

    if player1_score == 80 : 
        print("WOW you got a Ladder🙌")
        player1_score = 99

    if player2_score == 1 : 
        print("WOW you got a Ladder🙌")
        player2_score = 38

    if player2_score == 4 : 
        print("WOW you got a Ladder🙌")
        player2_score = 14

    if player2_score == 9 : 
        print("WOW you got a Ladder🙌")
        player2_score = 31

    if player2_score == 21 : 
        print("WOW you got a Ladder🙌")
        player2_score = 42

    if player2_score == 28 : 
        print("WOW you got a Super-Ladder🙌")
        player2_score = 84 
    
    if player2_score == 51 : 
        print("WOW you got a Ladder🙌")
        player2_score = 67

    if player2_score == 72 : 
        print("WOW you got a Ladder🙌")
        player2_score = 91

    if player2_score == 80 : 
        print("WOW you got a Ladder🙌")
        player2_score = 99

    if player1_score == 100:
        print(player1,"WON THE GAME...🤪")
        print(player1,"Score is:",player1_score)
        print(player2,"Score is:",player2_score)
        break
    elif player2_score == 100:
        print(player2,"WON THE GAME...🤪")
        print(player1,"Score is:",player1_score)
        print(player2,"Score is:",player2_score)
        break
    else :
        print("Round",i,"is over and Total Score is:")
        print(player1,"Score is:",player1_score)
        print(player2,"Score is:",player2_score)
        i = i + 1
    
