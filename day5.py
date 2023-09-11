# with open('123.txt','r') as f:
#
#
#     zz=f.readline(5)
#
#
#
# print(zz)



# 小明正在使用电脑编程
# 小明 人类

# 电脑 电脑类


# __init__  用作类的初始化


# __str__ 用作类的返回值



# __del__ 用作对象地址被释放后自动被调用
from typing import Union

class People(object):
    def __init__(self,name:str,age:int,height:float,hobby:Union[str,None]=None):
        self.name=name
        self.age=age
        self.height=height
        self.hobby=hobby

    def play_object(self):
        self.object1=Computer(50)
        print(self.name+'like play'+self.object1.log+str(self.object1.price))

    def not_play_object(self):
        self.object2=Computer(100)
        print(self.name+' not like play'+self.object2.log+str(self.object2.price))





class Computer(object):
    def __init__(self,price):
        self.log=input("请输入电脑的品牌:")
        self.price=price


    def __str__(self):
        return "hello _computer 被调用了"


    def __del__(self):
        print('wo bei gandiaol')


if __name__ == '__main__':
    # xiaoming=People('xiaoming',23,156.8)
    # xiaoming.play_object()
    # xiaoming.not_play_object()
    # print(xiaoming.object1)
    #
    ss=Computer(23)
    print(ss)
