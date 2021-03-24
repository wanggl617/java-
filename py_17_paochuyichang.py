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