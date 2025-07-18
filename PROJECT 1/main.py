import random

''' 1 for stone 
    -1 for paper
    0 for scissor '''

computer = random.choice([-1,0,1])
youin = input("ENTER YOUR CHOICE : ")
youDICT = {"st":1, "p":-1 , "sc":0}
revesreDICT = {1:"STONE",-1:"WATER", 0:"SCISSOR"}
you = youDICT[youin]

print("USER CHOICE:- " , revesreDICT[you])
print("COMPUTER CHOICE:- " , revesreDICT[computer])


if (computer == you):
    print("it is draw!")
else:
    if(computer == 1 and you == 0):
        print("YOU LOSE!")
    elif(computer == 1 and you == -1):
        print("YOU WIN!")
    elif(computer == 0 and you == -1):
        print("YOU LOSE!")
    elif(computer == 0 and you == 1):
        print("YOU WIN!")
    elif(computer == -1 and you == 1):
        print("YOU LOSE!")
    elif(computer == -1 and you == 0):
        print("YOU WIN!")
    else:
        print("SOMETHING WENT WRONG")
    