
# 继承出现同名的状态优先调用第一个状态

# cat_dog.__mro__ 查看调用类名的优先级
# class cat(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def cat_play(self):
#         print(self.name,'cat are playing')
#
#
# class dog(object):
#     def __init__(self, name, age,kkk):
#         self.name = name
#         self.age = age
#         self.kkk=kkk
#
#     def dog_play(self):
#         print(self.name,self.kkk, 'dog are playing')
#
#
# class cat_dog(cat,dog):
#     pass
#
# if __name__ == '__main__':
#     print(cat_dog.__mro__)