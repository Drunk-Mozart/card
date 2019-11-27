chara: str = "hello, python"
for i in chara:
    print(i)

# object function for String
print(len(chara))
print(chara.count("ell"))
print(chara.index("ell"))
print(chara.count("all"))

space_str = "\t\r\n"
print(space_str.isspace())

nun_str = "\u00b2"
print(nun_str.isdigit())
print(nun_str.isdecimal())
print(nun_str.isnumeric())

print(chara.startswith("hello"))
print(chara.endswith("python"))
print(chara.find("python"))
print(chara.replace("python", "world"))

poem = ["  登鹳雀楼\t\n",
        "wangzhi",
        "白日依山尽,",
        "黄河入海流.",
        "欲穷千里目,",
        "更上一层楼."]

for i in poem:
    print("|%s|" % i.strip().center(10, "*"))

# conbine & split

poem_split = "  登鹳雀楼\t\n wangzhi \r白日依山尽, 黄河入海流 欲穷千里目, 更上一层楼."
temp_poem = poem_split.split()

print(poem_split)
print(temp_poem)
for i in temp_poem:
    print("|%s|"%i.center(8,"x"))

result = "".join(temp_poem)
print(result)

num_str = "0123456789"
print(num_str[::-1])
print(num_str[::2])
print(num_str[0::-1])