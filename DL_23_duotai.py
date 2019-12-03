# 子类使用父类的同一个方法可以返回不同的结果，在子类下重写方法即可

class Dog:

    def __init__(self, name):

        self.name = name

        print("%s 是一只狗" % self.name)

    def dog_play(self):

        print("%s 只能在地上玩！" %self.name)


class XiaoTianDog(Dog):
    
    def dog_play(self):

        print("%s 可以在天上玩" % self.name)


class Person:

    def __init__(self, name):

        self.name = name
        print("%s 爱和狗玩" % self.name)

    def play_dog(self, dog):

        print("%s 和 %s 玩" % (self.name, dog.name))
        dog.dog_play()

dog = Dog("小狗")
xiaotiangou = XiaoTianDog("哮天犬")
xiaoming = Person("小明")
xiaoming.play_dog(dog)
xiaoming.play_dog(xiaotiangou)





        