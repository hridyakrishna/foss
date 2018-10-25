print("LETS PLAY ROCK,PAPER,SCISSOR..\n PLAYER 1:COMPUTER...\nPLAYER 2:______")
name=input("name: ")
player1_score=0
player2_score=0
import random
options=["ROCK","PAPER","SCISSOR"]
while(player1_score<10 and player2_score<10):
    tool=random.choice(options)
    print("player 1 chose")
    print(name," choose any tool.(r/p/s)")
    users_tool=input("Give your tool: ")
    if(users_tool=="r"):
        print("your choice:ROCK,\ncomputer's choice:",tool)
        if(tool=="ROCK"):
            print("thats same!Do it again\n\n\n")
        elif(tool=="SCISSOR"):
            print(name," blunt computers scissor\n")
            player2_score=player2_score+1
            print("your score:",player2_score," \ncomputer's score:",player1_score,"\n")
        else:
            print("computer wrapped ",name,"'s rock\n")
            player1_score=player1_score+1
            print("your score:",player2_score," \ncomputer's score:",player1_score,"\n")
    elif(users_tool=="p"):
        print("your choice:PAPER,\ncomputer's choice:",tool)
        if(tool=="ROCK"):
            print(name," wrapped computer's rock\n")
            player2_score=player2_score+1
            print("your score:",player2_score," \ncomputer's score:",player1_score,"\n")
        elif(tool=="SCISSOR"):
            print("computer cuts ",name,"'s paper\n")
            player1_score=player1_score+1
            print("your score:",player2_score," \ncomputer's score:",player1_score,"\n")
        else:
            print("thats same!Do it again\n\n\n")
    elif(users_tool=="s"):
        print("your choice:SCISSOR,\ncomputer's choice:",tool)
        if(tool=="ROCK"):
            print("computer blunt ",name,"'s scissor\n")
            player1_score=player1_score+1
            print("your score:",player2_score," \ncomputer's score:",player1_score,"\n")
        elif(tool=="SCISSOR"):
            print("thats same!Do it again\n\n\n")
        else:
            print(name, "cuts computer's paper\n")
            player2_score=player2_score+1
            print("your score:",player2_score," \ncomputer's score:",player1_score,"\n")
    else:
        print("choose from above options.")
if(player1_score>player2_score):
    print("COMPUTER WINS")
else:
    print(name,"WINS")
