# 许三多有一把AK47，可以开火，可以上子弹

class Gun:

    def __init__(self, model):
        self.model = model
        self.count = 0
        print("这是一把%s" % self.model)

    def add_bullet(self, count):

        self.count += count

    def fire(self):

        if self.count <= 0:
            print("没有子弹，无法开枪")
            return

        self.count -= 1
        print("%s You are on fire %d" % (self.model, self.count))


# ak47 = Gun("AK47")
# ak47.add_bullet(8)
# ak47.fire()


class Soldier:

    def __init__(self, name):
        self.name = name
        self.gun = None

    def shoot(self):
        if self.gun is None:
            print("没有枪，无法射击")
            return
        self.gun.add_bullet(50)
        self.gun.fire()

xusanduo = Soldier("许三多")
xusanduo.gun = Gun("AK47")
# xusanduo.gun.add_bullet(8)
xusanduo.shoot()