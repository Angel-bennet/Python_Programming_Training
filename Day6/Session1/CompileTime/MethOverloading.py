#Method overloading- fn with same name but different parameters

class demo:
    # def add(self,a):
    #     print(a)
    # def add(self,a,b): will not work in python
    #     print(a+b)
    def add(self,*num):
        print(sum(num))

obj=demo()
obj.add(10)
obj.add(10,90)