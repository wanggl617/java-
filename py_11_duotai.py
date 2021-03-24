class Person(object):
    def __init__(self,name):
        self.name=name
    
    def play_with_dog(self,Dog):
        print("%s 在和 %s 玩耍——————" % (self.name,Dog.name))
        Dog.play()
    
class Dog(object):
    def __init__(self,name):
        self.name=name
    def play(self):
        print("%s 在玩耍------" % self.name)
class Y_Dog(Dog):
    def play(self):
        print("%s 在玩耍-汪汪--"% self.name)

xiao_Y=Dog("原狗")
#xiao_Y=Y_Dog("原狗")
xiao_S=Person("小宋")
xiao_S.play_with_dog(xiao_Y)
