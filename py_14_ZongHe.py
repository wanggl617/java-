# 					Game
# ______________________________________________
# Game.top_score
# player_name
# ______________________________________________
# __init__(self,player_name):
# show_help():
# show_top_score(cls):
# start_game(self):
# ______________________________________________
class Game(object):
    #类属性top_score
    top_score=0
    @classmethod      #类方法， 用默认参数 cls.top_score 直接访问类属性 类似self
    def show_top_score(cls):
        print("当前最高分为：%d" % cls.top_score)
    @staticmethod     #静态方法，既不需要访问类属性，也不需要访问实例属性
    def show_help():
        print("游戏帮助信息")
    #实例属性 name 
    def __init__(self,name):
        self.name=name
    #实例方法 start_game
    def start_game(self):
        print("%s 开始游戏了"% self.name)
#1.查看帮助信息
Game.show_help()
#2.查看最高分
Game.show_top_score()
#3.创建玩家对象
player_1=Game("玩家1")
#4.开始游戏
player_1.start_game()
        