# try:
#     f=open('123.txt','r')
# except IOError as e:
#     print(e)
# else:
#     print('no 异常')
# finally:
#     print('all over')


# try  尝试进行执行  执行失败执行 except  finally
# 执行成功 执行else finally语句


# 规定被调用时只能导出all中存在的成员   一般配合__init__.py执行
# __all__=['main']
#
# class ShortInputException(Exception):
#     '''自定义的异常类'''
#     def __init__(self, length, atleast):
#         #super().__init__()
#         self.length = length
#         self.atleast = atleast
#
# def main():
#     try:
#         s = input('请输入 --> ')
#         if len(s) < 3:
#             # raise引发一个你定义的异常
#             raise ShortInputException(len(s), 3)
#     except ShortInputException as result:#x这个变量被绑定到了错误的实例
#         print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
#     else:
#         print('没有异常发生.')
#
#
# main()