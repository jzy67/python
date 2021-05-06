'''多重继承'''
# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass

'''定制类'''
# class Student(object):
#     def __init__(self,name):
#         self._name=name
#     def __str__(self):
#         return 'Students Object name(%s)'%self._name
#     __repr__=__str__
# print(Student('Machael'))

# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>10000:
#             raise StopIteration()
#         return self.a
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start==None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(x)
#                 a,b=b,a+b
#             return L
# for n in Fib():
#     print(n)
# f=Fib()
# print(f[:2])

# class Student(object):
#     def __init__(self):
#         self.name='Michael'
#     def __getattr__(self,attr):
#         if attr=='score':
#             return 99
#         if attr=='age':
#             return lambda:25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)
# s=Student()
# print('%s %s %d'%(s.name,s.score,s.age()))
# print(s.abc)

# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#     def __str__(self):
#         return self._path
#     __repr__ = __str__
# print(Chain().status.user.timeline.list)

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    def users(self,name):
        return Chain('%s/users/%s'%(self._path,name))
    __repr__ = __str__
print(Chain().users('michael').repos)

