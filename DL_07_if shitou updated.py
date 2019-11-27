import random
player = int(input("please input your choice 1-shitou, 2-jiandao, 3-bu: "))
computer = random.randint(1,3)
print("the player is %d, the computer is %d"%(player,computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer ==1)):
    print("Cgrate, you win!")
elif player == computer:
    print("equal")
else:
    print("you lose")
