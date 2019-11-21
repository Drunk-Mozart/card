card_list = []


def add_card():
    name = input("pls input the name you want to add:")
    gender = input("pls input gender of %s:" % name)
    job = input("pls input job of %s:" % name)
    age = input("pls input age of %s:" % name)
    card_list.append({"name": name, "gender": gender, "job": job, "age": age})
    print(card_list)


def search_card():
    name = input("pls input the name you want to search:")
    for card in card_list:
        if card["name"] == name:
            print(card["name"], card["gender"], card["job"], card["age"])
            change_card = input("是否需要修改: 1-是，0-否")
            if change_card:
                modify_card(card["name"], card["gender"], card["job"], card["age"])
            break
        else:
            print("%s is not in the card list" % name)


def show_card():
    for card in card_list:
        print(card["name"], card["gender"], card["job"], card["age"])


def modify_card(name, gender, job, age):
    if name:
        name = input("pls input the name you want to change:")
    if gender:
        gender = input("pls input gender of %s:" % name)
    if job:
        job = input("pls input job of %s:" % name)
    if age:
        age = input("pls input age of %s:" % name)
    print(name, gender, job, age)
    card_list.append({"name": name, "gender": gender, "job": job, "age": age})
    # card_list.append(name, gender, job, age)
