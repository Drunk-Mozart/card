# 许三多有一把AK47，可以开火，可以上子弹

class Gun:

    def __init__(self, model):
        self.model = model
        self.count = 0
        print("这是一把%s" % self.model)

    def add_bullet(self, count):

        self.count += count

    def fire():

        if self.count < 0:
            print("没有子弹，无法开枪")

        self.count -= 1
        print("You are on fire")


ak47 = Gun("AK47")
