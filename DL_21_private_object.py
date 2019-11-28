# 私有属性和私有方法

class Woman:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secrate(self):
        print("%s 的年纪是 %d" %(self.name, self.__age))

    def pr_secrate(self):
        self.__secrate()


xiaofang = Woman("xiaofang", 18)
# print(xiaofang.__age)
xiaofang.pr_secrate()

# 在外部调用私有方法和属性，_类名+私有方法，说明没有真正的私有

xiaofang._Woman__secrate()
print(xiaofang._Woman__age)

# 继承能否调用父类的私有属性和方法

class OldWoman(Woman):
    def print_name(self):
        print("你的名字是%s"%self.name)

    # def pr_age(self):

xiaowang = OldWoman("xiaowang", 18)
print(xiaowang.name)
xiaowang.print_name()
