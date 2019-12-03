class Game(object):

    rank = 0
    def __init__(self, player_name):
        self.name = player_name
        print("当前的游戏玩家是：%s" % self.name)

    @classmethod
    def show_rank(cls):
        print("最高分数是：%d" % cls.rank)

    @staticmethod
    def show_help():
        print("帮助信息")
    


    def startgame(self):
        print("%s 游戏开始！" % self.name)


Game.show_help()
Game.show_rank()
game = Game("小明")
game.startgame()