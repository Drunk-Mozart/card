# 通过类创建对象时，先调用new方法为对象创建内存空间，再通过初始化方法初始化对象

class Player(object):

    def __new__(cls, *args, **kwargs):

        print("创建对象，分配空间")
        instance = super().__new__(cls)
        return instance

    def __init__(self):

        print("播放器初始化")


player1 = Player()
player2 = Player()
print(player1)
print(player2)

# 创建单例对象，只需要控制new方法只返回一个值

class Music(object):

    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):

        print("创建对象，分配空间")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):

        if self.init_flag:
            return
        else:
            self.name = name
            print("%s 音乐初始化" %self.name) # 初始化方法会不断被调用，设立标记让初始化内容只执行一次
            self.init_flag = True


misuc1 = Music("音乐1")
misuc2 = Music("音乐2")
print(misuc1)
print(misuc2)

