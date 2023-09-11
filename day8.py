# class people(object):
#     def __init__(self):
#         self.name='dddd'
#         self.age='kkkkkk'
#         self.__money=50
#
#
#
#     def get_money(self):
#         return self.__money
#
#
#     def change_money(self,num):
#         self.__money=num
#
#
#
#
# class hxf(people):
#     def __init__(self):
#         super().__init__()
#
#
#
#
# hxf1=hxf()
# hxf1.change_money(100)
# print(hxf1.get_money())


# 类属性与实例属性
# class dog(object):
#     type='animal'
#     def __init__(self):
#         self.name='hhhhh'
#
#
#
#
# class dog_z(dog):
#     def __init__(self):
#         super().__init__()
#
#
#
#
# dog11=dog_z()
# print(dog11.type)