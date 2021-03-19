class Animal:

    def __init__(self):
        super().__init__()
    def eat(self):
        print("吃")
    
    def drink(self):
        print("喝")

    def run(self):
        print("跑步")
    
    def sleep(self):
        print("睡觉")

#创建Gog 类，使用继承
#子类 拥有父类的所有属性和方法
#然后子类根据 职责，封装自己独有的属性和方法
class Dog(Animal):
    def dark(self):
        print("汪汪汪")

#对父类方法重写1：全部重写
class X_Dog(Dog):
    #对Dog类中的dark() 方法，进行重写
    def dark(self):
        print("呜呜呜")

#对父类方法重写2：对父类进行扩展
class S_Dog(Dog):
    def dark(self):
        
        #1、针对子类特有的需求，编写代码
        print("我是小宋")
        #2、使用super(). 调用原本父类封装的方法
        super().dark()
        #3、增加子类需要的其他代码
        print("Shf")


# Xiao_t=Dog()
# Xiao_t.run()
# Xiao_t.bark()

tong=S_Dog()
tong.dark()