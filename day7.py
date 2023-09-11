# 通过使用类名调用父类方法 不重建父类对象

# class dog(object):
#     def __init__(self):
#         self.name='hhhhh'
#
#     def makedog(self):
#         print('i am a dog')
#
#
#
#
# class cat(object):
#     def __init__(self):
#         self.name='kkkkkk'
#
#     def makecat(self):
#         print('i am a cat')
#
#
#
# class cat_dog(cat,dog):
#     def __init__(self):
#         self.name='zzzzzz'
#
#     def old_make(self):
#         dog.__init__(self)
#         print(self.name)
#
#
#     def make_cat_dog(self):
#         print(self.name,'pppppppp')
#
#
#
# if __name__ == '__main__':
#     ppp=cat_dog()



# super   子类调用父类的方法

# class cat(object):
#     def __init__(self):
#         self.name='hhhh'
#         self.age=23
#         self.height=178
#
#
#
#     def make_dog(self):
#         print(self.name,self.age)
#
#
#
#
#
# class tiger(cat):
#     def __init__(self):
#         super().__init__()
#     def make_tiger(self):
#         super().make_dog()
#         print(self.name+'zzzz')
#
#
#
#
# tiger1=tiger()
# tiger1.make_tiger()