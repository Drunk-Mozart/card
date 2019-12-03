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

# 多继承，一个子类继承多个父类
class A:
    def __init__(self):
        print("You are beautiful!")

    def beautiful(self):
        print("You are beautiful!")

class B:
    def __init__(self):
        print("You are young")

    def young(self):
        print("You are young")

class C(A, B):
    pass

arthur = C() # 同样有init方法，但只会调用位置在先的，从先至后寻找，先找到的先调用，一直找不到就报错
arthur.beautiful()
arthur.young()

