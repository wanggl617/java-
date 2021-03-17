class Cat:

    def __init__(self,new_name):

        print("这是一个初始化方法")
        self.name=new_name
    def eat(self):
        print("%s 爱吃鱼" %self.name)
tom=Cat("TOM")
print(tom.name)
tom.eat()

jelf=Cat("JELF")
print(jelf.name)
jelf.eat()