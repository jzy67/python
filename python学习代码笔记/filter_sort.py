# #filter
# def is_palindrome(n):
#     s=str(n)
#     n=len(s)
#     for i in range(n):
#         if s[i]!=s[n-1-i]:
#             return False
#     return True
# output=filter(is_palindrome,range(1,1000))
# print(list(output))

# print(sorted([36,5,-12,9,12]))
# print(sorted([36,5,-12,9,-21],key=abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))
# #key作用在每一个元素上
# def by_name(t):
#     return t[0]
# def by_score(t):
#     return t[1]
# L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
# print(sorted(L,key=by_name),'\n',sorted(L,key=by_score,reverse=True))

# def f():
#     def g(i):
#         def d():
#             return i*i
#         return d
#     fs=[]
#     for i in range(1,4):
#         fs.append(g(i))
#     return fs
# f1,f2,f3=f()
# print(f1(),f2(),f3())

#匿名函数
# f=lambda x:x*x
# print(f(5))

# 装饰器Decorator
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('call '+func.__name__+'()')
#         return func(*args,**kw)
#     return wrapper
# @log
# def now():
#     print("2021")
# now()

# import functools
# def log(func):
#     def wrapper(*args,**kw):
#         print("begin call")
#         func(*args,**kw)
#         print("end call")
#     return wrapper
# @log
# def now():
#     print("2021-4-17")
# now()

# #偏函数
# import functools
# int2=functools.partial(int,base=2)
# print(int2('100'))

