# a=[2,3,4]
# s,x,c=a
# print(s,x,c)




# 字典拆包取key
# aa={'m':12,'k':23}
# d,f=aa
# print(d,f)



# 引用的问题
# a=100
#
# def test1(b):
#     b+=b
#
#
#
# test1(a)
# print(a)

# a=200
# b=a
# b+=b
# print(id(a))
# print(id(b))


# 可变数据类型  引用的传递  b+=  扩容   b=b+b  指向新的
# 不可变数据类型  指向新的内容
# a=[11,22]
#
# def test1(b):
#     b+=2*[11]
#
# test1(a)
# print(a)



# lambda
# sum=lambda x,y:x+y
# print(sum(2,3))


# def func(a,b,opt):
#     c=opt(a,b)
#     return a+b+c
#
#
# print(func(2, 3, lambda x, y: x + y))


# lambada用做内置函数的参数
# stus=[  {"name": "zhangsan", "age": 18},
#     {"name": "lisi", "age": 19},
#     {"name": "wangwu", "age": 17}]
#
# func=lambda x:x['name']
#
#
# stus.sort(key=func)
# print(stus)