# n1=255
# n2=1000
# print(str(hex(n1)),str(hex(n2)))
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>0:
#         return x
#     else:
#         pass
#         return  
# print(my_abs(-5))
# print(my_abs('2'))


# import math
# def move(x,y,step,angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx,ny#return is a tuple
# print(move(100,100,60,math.pi/6))


# import math
# def quadratic(a, b, c):
#     if (b**2-4*a*c>=0):
#         return (-b+math.sqrt(b**2-4*a*c))/(2*a), (-b-math.sqrt(b**2-4*a*c))/(2*a)
#     else:
#         return str(-b/(2*a))+" +/- "+str(math.sqrt(4*a*c-b**2)/(2*a))+"i"
# print(quadratic(1,3,-4))
# print(quadratic(1,2,2))
# def power (a,n=2):
#     s=1
#     while(n>0):
#         n-=1
#         s*=a
#     return s
# print(power(5),power(5,4))


# def calc(number):
#     sum=0
#     for n in number:
#         sum+=n*n
#     return sum
# print(calc([1,2,3]))
# print(calc((1,2,3)))


# def calc(*number):#参数接受的是一个tuple
#     sum=0
#     for n in number:
#         sum+=n*n
#     return sum
# print(calc(1,2,3))
# print(calc(*[1,2,3]))


# def person(name, age, **kw):#kw is a dict
#     print('name:',name, 'age:', age, 'other:', kw)
# person('michael',30)
# person('Bob',35,city='BeiJing')
# person("Adm",45,gender='man',job='engineer')
# extra={'city':'BeiJing','job':'engineer'}
# person("Jack",24,city=extra['city'],job=extra['job'])
# person("jack",24,**extra)


# def person(name,age,*,city,job):
#     print(name,age,city,job)
# person('j','21',city='Nanjing',job='student')


# def person(name,age,*,city='Beijing',job):# *后面是关键字参数
#     print(name,age,city,job)
# person('ja','24',job='engineer')

#递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(1))
# print(fact(3))

# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)

#汉诺塔
def move(n,a,b,c):
    if (n==1):
       print('move',a, '->', c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(4,'A','B','C')
     
