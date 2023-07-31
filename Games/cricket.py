import random as rd
import time

Ind = ["Rohit","Rahul","Virat","Hardik","Kunal"]
Pak = ["Warner","Stark","Max","Dexter","Jordan"]
teams = ["Ind","Pak"]
Toss_pos = ["Head","Tail"]
Toss_res = ["BAT First","BOWL First"]
print("Coin is Tossed...")
time.sleep(2)
print(rd.choice(teams), "calls", rd.choice(Toss_pos), "and choose to :", rd.choice(Toss_res))

ball_pos = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,4,4,4,6,6,6,6,"out","out","out","out","out","wide","wide","wide","no_ball","no_ball","no_ball","no_ball"]

team_score = 0
team_extras = 0
team_out = 0

ball_no = 1
while ball_no <= 6:
    print("Press ENTER to HIT a BALL")
    input()
    a = rd.choice(ball_pos)
    print(a)
    
    if a=="out":
        print("Better luck next time player OUT")
        team_out = team_out + 1
        ball_no = ball_no + 1
        # break
    

    elif a==1 or a==2 or a==3:
        team_score = team_score + a
        print("Team Runs :",team_score) 
        ball_no = ball_no + 1
        # break

    elif a==4:
        print("Ohho it's FOUR")
        team_score=team_score+a
        print("Team Runs :",team_score)
        ball_no = ball_no + 1
        # break

    elif a==6:
        print("Unbelievable SIX")
        team_score=team_score+a
        print("Team Runs:",team_score)
        ball_no = ball_no + 1
        # break

    else :
    #  a =="wide" or a =="no_ball":
        print("Team got Extra Runs")
        team_extras = team_extras+1
        team_score = team_score + 1


print("="*50)
print("Total Score :",team_score)
print("Extra Runs: ",team_extras)
print("Team Wickets: ",team_out)
    

