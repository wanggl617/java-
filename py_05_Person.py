class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return "我是%s，我的体重是%.2f公斤" %(self.name,self.weight)
    def run(self):
        print("跑步减肥")
        self.weight-=0.5
    def eat(self):
        print("吃东西增肥")
        self.weight+=1

X=Person("小明",75)
X.run()
X.eat()
X.eat()
print(X)
