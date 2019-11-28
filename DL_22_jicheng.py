# 通过子类对父类的继承，直接调用父类的方法

class Animals:

    def eat(self):
        print("吃")

    def run(self):
        print("跑起来")

# 狗从动物类派生，动物是基类，也是父类

class Dogs(Animals):

    def buk(self):
        print("汪汪叫")


xiaohuang = Dogs()
xiaohuang.eat()

# 子类的子类可以继承基类，继承的传递性

class BigDog(Dogs):

    def eye(self):
        print("三只眼")

# 方法重写，改写父类方法
    def buk(self):
        print("哦哦叫")
#  改写之后，从新调用父类方法
        super().buk()
        print("其他声音")

xiaobing = BigDog()
xiaobing.eat()
xiaobing.buk()