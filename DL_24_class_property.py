# 类的属性，与对象无关，与对象有关的属性应该记录在init方法中；


class Tool:

    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool1 = Tool("镰刀")
tool1 = Tool("锄头")

print(Tool.count)

# 但其实对象也可以调用这个属性，如果在对象本身没有找到这个属性，则向类查找

print(tool1.count)

# 不推荐使用对象调用类属性，因为如果对象属性被赋值语句改变

tool1.count = 5
print(tool1.count)
print(Tool.count)