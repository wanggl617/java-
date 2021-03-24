class Tool(object):
    #使用赋值语句定义类属性
    count=0   #count 就是类Tool特有的属性，就是类属性
    def __init__(self,name):

        self.name=name
        #通过 类名.count 访问类属性，并进行操作
        Tool.count+=1

tool_1=Tool("工具1")
tool_2=Tool("工具2")
#输出工具对象的总数
print(Tool.count)