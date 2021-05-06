# L=list(range(20))
# print(L[:10],'\n',L[-10:],'\n',L[:10:2],'\n',L[::5],'\n',L[:])
# d={'a':1,'b':2,'c':3}
# for k in d:
#     print(k)
# for v in d.values():
#     print(v)
# for k,v in d.items():
#     print(k,'=',v)
# print([k+"="+str(v) for k,v in d.items()])
# from collections.abc import Iterable
# print(isinstance([1,2,3], Iterable))
# for i, value in enumerate((1,2,3)):
#     print(i, value)
# for x,y in [(1,3),(2,8),(5,5)]:
    # print(x,y)
# print([x*x for x in range(1,11)])
# print([x*x for x in range(1,11) if x%2==0])
# print([m+n for m in 'ABC'  for n in 'XYZ'])
# l1=['Hello','world',18,'Apple',None]
# l2=[s.lower() for s in l1 if isinstance(s,str)]
# print(l2)

# 生成器
# g = (x*x for x in range(10))
# print(next(g),next(g))
# for n in g:
#     print(n)
# print(next(g))
# def odd():
#     yield 1
#     yield 2
#     yield 3
# n=odd()
# print(next(n))
# print(next(n))

# 杨辉三角
# def triangles():
#     l=[1]
#     while 1:
#         yield l
#         l=[a+b for a,b in zip(l,l[1:])]
#         l.insert(0,1)
#         l.append(1)
# n=0
# res=[]
# for t in triangles():
#     print(t)
#     n=n+1
    # if n ==10:
    #     break