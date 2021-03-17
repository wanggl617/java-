class Cat:
    '''这是一个猫类'''

    def eat(self):
        #哪一个对象调用的方法，self就是其的引用
        print("%s 爱吃鱼" % self.name)


tom=Cat()
tom.name="TOM"
tom.eat()

jelf=Cat()
jelf.name="JELF"
jelf.eat()
