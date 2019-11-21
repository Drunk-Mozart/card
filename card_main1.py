import card_tool1

while True:
    # show selection interface
    print(50 * "*")
    print("1-查询名片")
    print("2-新增名片")
    print("3-显示所有名片")
    print("0-退出程序")
    print(50 * "*")
    str_input = input("please input the number you want: ")
    # 新增名片, 查询名片，显示名片
    if str_input in ["1", "2", "3"]:
        # pass
        if str_input == "1":
            print("查询名片")
            card_tool1.search_card()
        #     修改名片
        #     print("请输入是否需要修改：1-是，0-否")
        elif str_input == "2":
            print("新增名片")
            card_tool1.add_card()
        else:
            print("显示所有名片")
            card_tool1.show_card()
    elif str_input == "0":
        print("程序一退出")
        break
    else:
        print("input the wrong number")
