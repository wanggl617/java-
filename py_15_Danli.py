class MusicPlayer(object):
    instance=None
    def __new__(cls,*arg,**kwargs):
        #1.判断类属性是否为空
        if cls.instance is None:
            #2.调用父类方法，为第一个对象分配空间
            cls.instance=super().__new__(cls)
        #3.返回类属性保存的对象引用
        return cls.instance
player_1=MusicPlayer()
player_2=MusicPlayer()
print(player_1)
print(player_2)
#两个对象的内存空间一样。