while True:
    # show selection interface
    print(50 * "*")
    print("1-查询名片")
    print("2-新增名片")
    print("3-显示所有名片")
    print("0-推出程序")
    print(50 * "*")
    str_input = input("please input the number you want: ")
    if str_input in ["1", "2", "3"]:
        pass
    elif str_input == "0":
        break
    else:
        print("You've input an error number! Pls try again.")

print("end program")
