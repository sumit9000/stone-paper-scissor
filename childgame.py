 # Stone paper scissor game using python.
 #
 # Author: Sumit Kumar
 # https://github.com/sumit9000
 #
 # GitHub Link: https://github.com/sumit9000/stone,paper,scissor
 # Date:10.10.2021 sunday

# code 

# intialising module
import random
# printf statment
print("The game will be total of 10 rounds\nPress: 's' for stone or 'p' for paper or 'sc' for scissor")
# variable intialisation
i=0
win=0
lost=0
draw=0
# intialising while loop uptill 10 round get completed
while i<10:
    lst=["stone", "paper", "scissor"]
    choice=random.choice(lst)
    n=input("\nEnter your choice: ")
    # stone is the choice for computer
    if choice=="stone":
        if n=="s":
            print("Computer's choice: ",choice,"\n***Round Draw***!!!")
            draw+=1
        elif n=="p":
            print("Computer's choice:",choice,"\n***You have win this round***!!!")
            win+=1
        elif n=="sc":
            print("Computer's choice:",choice,"\n***You have lost this round***!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    # paper is the choice for computer
    elif choice=="paper":
        if n=="p":
            print("Computer's choice:",choice,"\n***Round Draw***!!!")
            draw+=1
        elif n=="s":
            print("Computer's choice:",choice,"\n***You have lost this round***!!!")
            lost+=1
        elif n=="sc":
            print("Computer's choice:",choice,"\n***You have win this round***!!!")
            win+=1
        else:
            print("You have entered a wrong choice")
    # scissor is the choice for computer
    else:
        if n=="sc":
            print("Computer's choice:",choice,"\n***Round Draw***!!!")
            draw+=1
        elif n=="s":
            print("Computer's choice:",choice,"\n***You have win this round***!!!")
            win+=1
        elif n=="p":
            print("Computer's choice:",choice,"\n***You have win this round***!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    print("Left-over round number: ",10-i)
    # User dashboard
    a=f"\nTill now the score is:\nYou: {win}\nComputer: {lost}\nDraw: {draw}"
    print(a)
    i+=1
# ```Final result```
if i==10:
    if win>lost:
        print("\nWinner!!! You have won the game")
    elif lost>win:
        print("\nGame Over!!! You have lost the game")
    else:
        print("\nGame Draw!!!")