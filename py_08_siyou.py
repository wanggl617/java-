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
#print(Xiao_t.__age)

#可以执行， 在对象的方法内部，可以访问其私有属性
Xiao_t.secret()