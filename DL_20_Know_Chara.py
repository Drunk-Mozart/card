# print("hello world")
# msg = "hello world"

poem = ["登鹳雀楼⑴","白日依山尽⑵,","黄河入海流。","欲穷千里目⑶，","更上一层楼⑷."]


for i in poem:
    print(i)

# public method for object like list, 元组，dict, string

temp_list = [1,2,3,4]
print(1 in temp_list)
temp_list.extend([7.8])
print(temp_list)
print(temp_list.append([1, 2]))
print(temp_list.extend([1, 2]))

a_list = [5,6]
b_list = temp_list + a_list

print(b_list)
print(4*a_list)

temp_dic = {"a":1,"b":2,"c":3}
temp_dic1 = {"d":4}
# print(temp_dic+temp_dic1) - 不能用extend,append,+方法
print(1 in temp_list)