class Human:
    # 属性
    gender = ["male", "female"]
    name = ["zhangsan", "lisi", "wangwu"]

    # 方法
    def walk(self):
        print("正在走路")

    def cook(self):
        print("正在做饭")


arthur = Human()

print(Human.__dict__)
print(arthur.__dict__)
print(int)
print(Human)