xiaoming = {"name": "xiaoming",
            "age": 18,
            "height": 1.75,
            "gender": True}

print(xiaoming)

# get value
print(xiaoming["name"])

# add value
xiaoming["hobby"] = "basketball"
xiaoming["name"] = "xiaoxiaoming"
print(xiaoming)

# delete value
xiaoming.pop("name")
print(xiaoming)

# count
print(len(xiaoming))

# append
temp_xiaoming = {"love": "xiaohuang"}
xiaoming.update(temp_xiaoming)
print(xiaoming)

# loop
for k in xiaoming:
    print("%s:%s" % (k, xiaoming[k]))

list_xiaoming = [xiaoming,temp_xiaoming]
for i in list_xiaoming:
    for k in i:
        print("%s:%s"%(k, i[k]))

print(list_xiaoming)