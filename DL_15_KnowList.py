name_list = ["zhangsan", "lisi", "wangwu"]

# know value
print(name_list[2])

# know index
print(name_list.index("wangwu"))

# modify
name_list[1] = "maliu"

# add
name_list.append("lishi")
name_list.insert(1,"xiaomei")

# extend list
temp_list = ["huang","long"]
name_list.extend(temp_list)

# remove from list
name_list.remove('lishi')
name_list.pop(1)
name_list.pop()
 # name_list.clear()
del name_list[1]

name = "zhangsan"
del name

print(name_list)

print(name_list.sort())
num_list = [3,2,1,4,6]
print(num_list)
num_list.sort(reverse=True)
print(num_list)

print(name_list)
print(len(name_list))
print(name_list.count('lishi'))

for name in name_list:
    print("this is my name: %s" %name)

