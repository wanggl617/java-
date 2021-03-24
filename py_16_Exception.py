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