player = int(input("please input your choice 1-shitou, 2-jiandao, 3-bu: "))
computer = 1
if player == 1:
    print("pingshou, try again!")
    player = int(input("please input your choice 1-shitou, 2-jiandao, 3-bu: "))
    if player == 2:
        print("you loss")
    elif player == 3:
        print("you win!")
    else:
        print("input error")
elif player == 2:
    print("you loss")
elif player ==3:
    print("you win!")
else:
    print("input error")