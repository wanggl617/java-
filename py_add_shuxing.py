class Cat:
    '''这是一个猫类'''

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")

tom=Cat()
#可以使用 .属性名  利用赋值语句添加，
tom.name="TOM"

tom.drink()
tom.eat()
print(tom)

lazy_cat=Cat()
lazy_cat.drink()
lazy_cat.eat()
print(lazy_cat)