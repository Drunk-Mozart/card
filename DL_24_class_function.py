# 如果不需要调用实例属性，则可以直接定义类方法或者静态方法

# 调用类属性的类方法@classmethod

class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量：%d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1

tool = Tool("斧头")

Tool.show_tool_count()

# 静态方法

class Dog(object):

    @staticmethod
    def run():

        print("小狗要跑")

Dog.run()