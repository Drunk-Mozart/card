# def add(name,gender,job,age):
# temp_list = []
# name = input("pls input the name you want to add:")
# gender = input("pls input gender of %s:" % name)
# job = input("pls input job of %s:" % name)
# age = input("pls input age of %s:" % name)
# card_list = temp_list.append({"name": name, "gender": gender, "job": job, "age": age})
# print(card_list)
# return card_list


# test for search name in card list
card_list = [{"name": "arthur", "gender": "male", "job": "auditor", "age": "18"},
             {"name": "alex", "gender": "male", "job": "auditor", "age": "18"}]

for card in card_list:
    if card["name"] == "arthur":
        print(card)
        break
    else:
        print("not in the list")

a = 2
print(id(a))
b = a
print(id(b))


def id_num(num):
    result = "hello"
    print("the address of num is %d" % id(num))
    print("the address of num is %d" % id(result))
    return result


id_num(a)

c = id_num(b)
print(id(c))
