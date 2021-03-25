##### 1、**类和对象的关系：**

1、**类是模板，**对象是根据类这个模板创建出来的。应该是先有类，再有对象，

2、类只有一个，对象可以有很多个。且不同对象的属性可以各不相同。 

3、类中定义了什么 **属性 和 方法**，对象中就有什么属性和方法，不可能多，也不可能少。



##### **2、类的设计**

在面向对象开发之前，进行需求分析，确定有哪些类，一般有很多个类。

**一个类应该包含三要素**

**类名  属性  方法**



例：**小明**今年18岁，身高**1.75m**，每天早上**跑**步，**吃**东西。

类名：person类；1

属性：age,height;

方法：run(),eat();



##### 3、在python 中定义包含方法的类：

```python
class 类名:
    def Methd_1(self,参数列表):
        pass
    def Methd_2(self,参数列表):
        pass
    '''第一个参数必须是self'''
```

​	

```python
class Cat:
    '''这是一个猫类'''

    def eat(self):
        #哪一个对象调用的方法，self就是其的引用
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")

#等号右边创建对象，等号左边对新创建的对象进行引用
tom=Cat()
tom.drink()
tom.eat()
```

**对于引用的强调，**

在Python中创建对象之后  **tom** 变量中仍然记录 对象在内存的地址

tom=Cat()  就是tom**变量** 引用了新建的猫**对象**

```
print(tom)   可以输出tom变量的内存地址
```



##### 4、**一个类，可以创建多个对象**

```python
#创建一个猫类
tom=Cat()
tom.drink()
tom.eat()
#输出tom变量的内存地址
print(tom)

#再创建一个猫类
lazy_cat=Cat()
lazy_cat.drink()
lazy_cat.eat()
print(lazy_cat)

#两个猫类  tom 和 lazy_cat 是两个不同的对象  即可以有一个类，但是可有创建多个对象
```



##### 5、**设置对象属性**

```python
tom=Cat()
#可以使用 .属性名  利用赋值语句添加，
tom.name="TOM"

'''不过一般这种方法是，临时加入一两个属性，一般不推荐这种方法'''

```



##### 6、self的使用 

```python
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

```

![image-20210317101856148](C:\Users\王国林\AppData\Roaming\Typora\typora-user-images\image-20210317101856148.png)

每当一个对象调用类的方法，

self就是其引用，当tom调用时，self就是tom, jelf调用时，self就是jelf

**在方法内部**

使用  **self.**可以访问对象的属性，

使用 **self.**可以调用其他的对象方法。



##### 7、初始化方法

当使用  **类名()** 创建对象时，会自动执行一下操作：

```
	1.为对象再内存中分配空间  ——创建对象

	2.为对象的属性 设置初始值  ——初始化方法（init）

这个初始化方法就是  __init__方法
```

**这个方法，就是专门用来定义一个类具体有哪些属性方法**

使用初始化方法，加self 封装类的属性：

```python
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
```



##### 8.封装

**封装—将属性和方法封装到一个抽象的类中，**

外部使用类创建对象，然后对象调用方法；

对象的方法的细节都封装在类的内部。



需求分析：

```
小明体重  75  公斤
小明每次跑步会减肥 0.5 公斤
小明每次吃东西增加 1  公斤
```

首先 ：名词提炼 ：小明  体重  （属性：name , weight）

动词：跑步，吃  （方法：run , eat)

```python
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

```

![image-20210317113617350](C:\Users\王国林\AppData\Roaming\Typora\typora-user-images\image-20210317113617350.png)

**有同一个类创建的多个对象，他们之间的属性互不干扰**



**实例：摆放家具**

需求：

```
1.房子(house)有 户型，总面积，家具名称列表
	新房子没有任何家具
2.家具(Houseltem)有 名字， 和占地面积，其中
	席梦思占地 4 平米
	衣柜占地  2  平米
	餐桌占地  1.5 平米
3.将以上三件家具 添加到房子中
4.打印房子时，要求输出：户型，总面积，剩余面积，家具名称列表
______________________________________________________
家具类 HouseItem
有两个属性  name  area 
______________________________________________________
房子类 House
有四个属性： house_type , area, free_area, item_list
一个方法，add_item()
______________________________________________________

```

```python
class HouseItem:

    def __init__(self,name,arae):
        self.name=name
        self.area=arae

    def __str__(self):
        return "%s 占地 %.2f" % (self.name,self.area)
    
class House:

    def __init__(self,House_type,area):
        self.House_type=House_type
        self.area=area
        self.free_area=area
        self.item_list=[]
    
    def add_item(self,item):
        if(item.area<=self.free_area):
            self.item_list.append(item.name)
            self.free_area=self.free_area-item.area
    
    def __str__(self):
        return ("%s 总面积为%.2f,\n剩余面积为%.2f,\n家具名称列表%s\n" 
                % (self.House_type,self.area,self.free_area,self.item_list))

Xi_ms=HouseItem("席梦思",4)
Yigui=HouseItem("衣柜",2)
Canzhuo=HouseItem("衣柜",1.5)

Beijing_H=House("两室一厅",60)
Beijing_H.add_item(Xi_ms)
Beijing_H.add_item(Yigui)
print(Beijing_H)
```



**实例：士兵突击**

一个对象的属性可以是 另外一个类创建的对象。

需求：

```
1.士兵 许三多 有一把AK
2.士兵 可以开火
3.枪能够 发射子弹
4.枪可以 装填子弹 ——（增加子弹数量）
______________________________________________________
soldier
属性 name  gun 
方法 fire()
______________________________________________________
Gun
属性 model   bullet_count
方法 add_bullet()
	shoot()
______________________________________________________
士兵开火实质上是枪发射
```

**开发士兵类：**
假设：每个新兵都没有枪。

在定义属性时，如果 **不知道设置什么初始值**，可以设置为 **Node**

​	None **关键字** 表示什么都没有

​	表示一个空对象，没有方法和属性，是一个特殊的常量

​	可以将None赋值给任何一个变量

```python
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
#创建一把枪对象 AK47   
AK=Gun("AK47")
#创建一个士兵对象 许三多
sol=Soldier("许三多")
#把枪给许三多  士兵类的对象的一个属性，可以是另外一个类的对象
sol.gun=AK
sol.fire()

```



##### 9、身份运算符

```python
is  判断两个变量的引用对象 是否为同一个
==  判断两个 引用变量的值是否相等

a = [1, 2, 3]
b = [1, 2, 3]

b is a     False
b == a     True
```



##### 10、私有属性和私有方法

属性名或者方法名之前加两个 下划线 __

```python
class   Women:

    def __init__(self,name):
        self.name = name
        #age属性不需要外部输入

        #age时私有属性
        self.__age =18
    
    def secret(self):
        print(" %s 的年龄时 %d" % (self.name,self.__age))

'''方法名之前加 __ 为私有方法，
    def __secret(self):
        print(" %s 的年龄时 %d" % (self.name,self.__age))
'''

Xiao_t=Women("小童")
#私有属性，外部无法访问，程序无法执行
print(Xiao_t.__age)

#可以执行， 在对象的方法内部，可以访问其私有属性
Xiao_t.secret()
```

**间接访问**

父类**公有**方法，**内部**可以访问**自己的私有属性和私有方法**，

子类可以调用/访问**父类的公有方法**，

这样就**间接**的，在**子类的方法**中访问到了**父类的私有属性和私有方法**



##### 11、继承

**封装**：根据职责  将  **属性和方法**  封装到一个抽象的**类**中

**继承**：**实现代码的重用**，相同的代码不需要重复编写

**多态**：不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活性



**01、单继承**

**继承**：子类拥有父类的所有属性和方法。

![image-20210319104152001](C:\Users\王国林\AppData\Roaming\Typora\typora-user-images\image-20210319104152001.png)

**方法重写**：

1、**当子类的所需要的方法**，父类已有，但并不适用，可以进行**方法重写**;

2、**子类的方法包含父类的方法**，即父类的方法不够了，需要**扩展父类**

```python
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

tong=X_Dog()
tong.dark()
```



##### 12、多继承

概念：

​	一个**子类** 可以拥有**多个父类**，并且拥有所有父类的 属性 和 方法

**注意：**一般要尽量**避免**父类之间存在 **属性名/方法名相同**的情况，这种情况下使用多继承，一般先继承哪个，就使用哪个



##### 13、多态

不同的子类对象，调用相同的父类方法，产生不同的执行结果，

​	多态可以增加代码的**灵活性**，

​	以 **继承和重写父类方法** 为前提

```python
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

```



##### 实例：

1.面向对象开发的 **第一步**是设计 类。

2.使用 **类名()** 创建对象，创建对象的动作有两步：

​	1）在内存中为对象分配空间，

​	2）调用初始化方法 `__init__`为对象初始化。

3.对象创建后，内存中就有了一个对象 实实在在的存在——**实例**

![image-20210323102951972](C:\Users\王国林\AppData\Roaming\Typora\typora-user-images\image-20210323102951972.png)



##### 14、类属性，类方法

概念： 收首先 类也是一种特殊的对象，可以称之为类对象，所以类也可以有自己特有的属性，方法，类的属性叫做，**类属性**，

​	**类属性**，就是给类对象定义的属性；

​	通常用来记录 与这个类相关的 特征；

​	类属性 不会用于记录 具体对象的特征。



**实例需求：**

- 定义一个工具类；
- 每件工具都有自己的`name`
- **需求**——知道这个类，创建了多少工具对象.

```python
#				Tool
#____________________________________
#Tool.count
#name
#____________________________________
#__init__(self,name)
#____________________________________

class Tool(object):
    #使用赋值语句定义类属性
    count=0
    def __init__(self,name):

        self.name=name
        #通过 类名.count 访问类属性，并进行操作
        Tool.count+=1

tool_1=Tool("工具1")
tool_2=Tool("工具2")
#输出工具对象的总数
print(Tool.count)
```



**类方法** 就是针对类对象所定义的方法。

在类方法内部，可以直接访问类属性，或者调用其他的类方法。

**语法如下**：

```c++
@classmethod
   def [类方法名](cls):
		pass
```

​	类方法 需要修饰器 `@classmethod`来标识；

​	类方法的第一个参数为 `cls`

​		由哪一类调用的方法，方法内的`cls`就是哪一个类的引用

​		这个参数和实例方法的第一个参数 `self`类似

​		使用其他名称也可以，不过习惯为`cls`

通过` 类名.`来调用 **类方法**，

**在方法内部**： 

​	可以通过 `cls.`访问类属性，或者调用其他的类方法



**实例需求：**

- 定义一个工具类
- 每件工具都有自己的`name`
- **需求**——在类 封装一个 `show_tool_count`的类方法，输出使用当前这个类创建的对象的数量。

```python
					Tool
_________________________________________________
Tool.count
name
_________________________________________________
__init__(self,name)
show_tool_count(cls)
_________________________________________________

class Tool(object):
    #使用赋值语句定义类属性
    count=0   #count 就是类Tool特有的属性，就是类属性

    #声明使用类方法，
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量：%d" % cls.count)#cls. 直接调用类属性
    

    def __init__(self,name):

        self.name=name
        #通过 类名.count 访问类属性，并进行操作
        Tool.count+=1

tool_1=Tool("工具1")
tool_2=Tool("工具2")
#调用类方法
Tool.show_tool_count()  #不需要传参数，类似self

```

 

**综合案例：**

需求

1.设计一个`game`类

2.属性：

​	定义一个类属性 `top_score`记录游戏的历史最高分

​	定义一个实例属性`player_name`记录当前游戏的玩家姓名

3.方法：

​	**静态方法**`show_help`显示游戏的帮助信息

​	**类方法**`show_top_score`显示历史最高分

​	**实例方法**`start_game`开始当前玩家的游戏

4.主程序步骤

​	1)查看帮助信息

​	2)查看历史最高分

​	3)创建游戏对象，开始游戏

```python
					Game
______________________________________________
Game.top_score
player_name
______________________________________________
__init__(self,player_name):
show_help():
show_top_score(cls):
start_game(self):
______________________________________________

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
```

**小结**

1.实例方法 ——方法内部需要访问 **实例属性**

​	实例方法也可以使用 `[类名].` 访问类类属性

2.类方法——方法内部 **只需要** 访问 类属性

3.静态方法——方法内部 **不需要**访问实例属性，也不需要访问类属性



#####  15、单例

**单例设计模式**

​	目的——让类创建的对象，在系统中只有**唯一的一个实例**

​	每一次执行 `类名（）`返回的对象，**内存地址是相同**的。

**应用场景**：

音乐播放器

打印机

……



 单例实现：

1.定义一个类属性，初始值为`None`，用于记录单例对象的引用

2.重写`__new__`方法，  `__new__`方法，为内置方法，在对类进行实例化时，会自动调用`__new__`方法，为对象分配内存空间，

​	在重写`__new__`方法时，必须返回`super().__new__(cls)`.

3.用类属性来记录，为对象分配的内存空间地址。

即：![image-20210323162933762](C:\Users\王国林\AppData\Roaming\Typora\typora-user-images\image-20210323162933762.png)

```python
class MusicPlayer(object):
    instance=None
    def __new__(cls,*arg,**kwargs):
        #1.判断类属性是否为空
        if cls.instance is None:
            #2.调用父类方法，为第一个对象分配空间
            cls.instance=super().__new__(cls)
        #3.返回类属性保存的对象引用
        return cls.instance
```



##### 16.异常

根据错误类型捕获异常：

```python
try:
    #提示输入一个整数
    num=int(input("输入一个整数"))
    result=8/num

    print(result)
except ValueError:
    print("输入整数")
except ZeroDivisionError:
    print("除0错误")
#捕获未知错误
#因为不可能预判到所有的错误类型。
except Exception as ex:
    print("未知错误%s" % ex)
```



**异常处理的完整语法：**

```c++
try:
    #尝试执行的代码
    pass
except EX_1:
    #针对错误类型1，对应的代码处理
    pass
except EX_2:
    #针对错误类型2，对应的代码处理
    pass
....
except Exception as ex:
    #除已知错误类型的，其他未知错误
    print(ex)
else:
    #没有异常才会执行的代码
    pass
finally:
    #无论是否由异常，都会执行的代码
    print("")
```

异常的传递:

当在一个**函数/方法**中出现异常，异常会向上传递，传递到调用它的 **函数/方法**  一直传递到 主程序，然后结束程序。

所以利用异常的传递性，可以只需要在主程序上设置异常捕获即可。



**异常主动抛出案例：**

需求：

​	定义`input_password`函数，提示用户输入密码

​	如果用户输入长度<8 ,抛出异常

​	如果用户输入长度>=8 返回输入的密码

```python
def input_password():
    #1.提示用户输入密码
    pwd = input("输入密码")
    #2.判断密码长度
    if len(pwd)>=8:
        return pwd
    ex = Exception("密码长度不够")
    #主动抛出异常
    raise ex
try:
    print(input_password())
except Exception as result: #捕获上面抛出的异常
    print(result)
```



##### 17.模块

1）模块导入：

```
import 模块名1，模块名2
```

在导入模块时，每个导入应该独占一行

导入之后通过`模块名.`使用 模块提供的工具，——全局变量，函数，类

如果通过`from..import `不需要通过  `模块名.`的方式，可以直接调用。



2）问题：

模块中无缩进符的，可以直接执行的代码，如：`print("  ")`也会被导入，并在新的文件中直接执行.



所以，在开发过程中，一些测试 代码，只需要在模块内执行，而被导入到其他文件中不需要执行。

```python
def main():
   #添加测试代码
    pass
if __name__ == "__main__":
	main()
    
```



##### 18、包

概念：

​	包是一个包含多个模块的特殊目录

​	目录下有一个特殊文件`__init__.py`

​	包的命名方法和变量名一致，**小写字母+_**

好处：

​	使用`import 包名`可以一次性导入包中所有模块

__init__.py

要在外界使用包中的模块，需要在`__init__.py`中**指定对外界提供的模块列表**

```python
#从  当前目录  导入  模块列表
from . import [模块1]
from . import [模块2]
```



##### 19、**发布模块，安装模块**

**制作模块压缩包**

1）创建 setup.py 文件：

```python
from distutils.core import setup

setup(name="[包名]",
     version="1.0",#版本
     description="[描述信息]",
     long_description="[完整的描述信息]",
     author="[作者]",
     author_email="[作者邮箱]",
     py_modules=["文件1",
                 "文件2"])

```

2）构建模块

```
$  python3 setup.py build
```

3）生成发布的压缩包

```
$  python3 setup.py sdist
```

**安装模块**

```
$  tar -zxvf [压缩包名].tar.gz
$  sudo python3 setup.py install
```

**卸载模块**

从安装目录下，包安装的模块的目录删除

```
$ cd uer/local/lib/python3.6/dist-packages/
$ sudo rm -r [包名]*
```



##### 20、文件操作

| 序号 | 函数/方法 | 说明                         |
| ---- | --------- | ---------------------------- |
| 01   | open      | 打开文件，并返回文件操作对象 |
| 02   | read      | 将文件内容读取到内存         |
| 03   | write     | 将指定内容写入文件           |
| 04   | close     | 关闭文件                     |

`open `函数负责打开文件，并且返回**文件对象**

`read/write/close`三个方法都需要通过 **文件对象** 来调用