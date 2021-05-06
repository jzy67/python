# from functools import reduce
# def fn (x,y):
#     return x*10+y
# def char2num(s):
#     return {'0':0,'1':1,'2':2,'3':3,'4':4}[s]
# print(reduce(fn,map(char2num,'1023')))


# def normalize(name):
#     return name.capitalize()#首字母大写，其余小写
# L1=['adam','LISA','barT']
# L2=list(map(normalize,L1))
# print(L2)

# from functools import reduce
# def prod(L):
#     def multi(x,y):
#         return x*y
#     return reduce(multi,L)
# print('3*5*7*9=',prod([3,5,7,9]))

from functools import reduce
def str2float(s):
    n=s.index('.')
    def strfloat(z):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7}[z]
    def fn (x,y):
        return x*10+y
    return reduce(fn,map(strfloat,s[:n]))+reduce(fn,map(strfloat,s[n+1:]))/(10**len(s[n+1:]))
print(str2float('123.456'))