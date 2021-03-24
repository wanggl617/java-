class A:
    def text1(self):
        print("11111")

class B:
    def text2(self):
        print("222")

class C(A,B):
    pass
c=C()
c.text1()
c.text2()
