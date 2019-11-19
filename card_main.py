card_list = [{"name": "arthur", "gender": "male", "job": "auditor", "age": "18"},
             {"name": "alex", "gender": "male", "job": "auditor", "age": "18"}]
while True:
    # show selection interface
    print(50 * "*")
    print("1-查询名片")
    print("2-新增名片")
    print("3-显示所有名片")
    print("0-退出程序")
    print(50 * "*")
    str_input = input("please input the number you want: ")
    if str_input in ["1", "2", "3"]:
        if str_input == "1":
            name = input("pls input the name you want to search:")
            for card in card_list:
                if card["name"] == name:
                    print(card)
                    break
            else:
                print("name not in the card list")
            # pass
        elif str_input == "2":
            name = input("pls input the name you want to add:")
            gender = input("pls input gender of %s:" % name)
            job = input("pls input job of %s:" % name)
            age = input("pls input age of %s:" % name)
            card_list.append({"name":name,"gender":gender,"job":job,"age":age})
            # pass
        else:
            print(card_list)
            # pass
    elif str_input == "0":
        break
    else:
        print("You've input an error number! Pls try again.")

print("end program")
