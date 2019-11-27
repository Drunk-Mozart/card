list_tuple = ("zhangsan", 19, 1.70)
print(list_tuple[0])
print(list_tuple[1])
print(list_tuple[2])
print(type(list_tuple))

for name in list_tuple:
    print(name)

print(list_tuple.count(19))
print(len(list_tuple))
print(list_tuple)

print("%s is %d age, %.2f height" % ("xiaoming", 19, 1.78))

intro_ming = "%s is %d age, %.2f height" % list_tuple

print(intro_ming)