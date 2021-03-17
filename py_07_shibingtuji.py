class Gun:
    #枪的属性需要从外部输入，但是如果默认每把枪初始子弹都为0，
    # 都需要装填子弹，即可不需要外部输入
    def __init__(self,model):
        self.model=model
        self.bullet_count=0

    def add_bullet(self,count):
        self.bullet_count+=count
    
    def shoot(self):
        #要判断子弹数量
        if(self.bullet_count>0):
            #发射子弹
            self.bullet_count-=1
            print("%s 在射击>>>>>[%d]"% (self.model,self.bullet_count))

class Soldier:
    #假设新兵都没有枪
    def __init__(self,name):
        self.name=name
        #初始化的时候 赋值None
        self.gun=None

    def fire(self):
        #self.gun时一个 Gun类的对象，可以调用 Gun类的方法
        if self.gun!=None:
            self.gun.add_bullet(60)
            print("我是%s,GO GO GO" % self.name)
            self.gun.shoot()
            return
        print("我没有枪")
#创建一把枪对象 AK47   
AK=Gun("AK47")
#创建一个士兵对象 许三多
sol=Soldier("许三多")
#把枪给许三多  士兵类的对象的一个属性，可以是另外一个类的对象
sol.gun=AK
sol.fire()
