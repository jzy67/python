# '''type'''
# def fn(self,name='world'):
#     print("Hello,%s."%name)
# Hello=type('Hello',(object,),dict(hello=fn))
# h=Hello()
# print(type(Hello))
# print(type(h))

# '''metaclass'''
# '''没看懂 空'''

'''try'''
# try:
#     print('try...')
#     r=10/0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r=10/int('a')
#     print('result:',r)
# except ValueError as e:
#     print('except:',e)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r=10//3
#     print('result:',r)
# except ValueError as e:
#     print('except:',e)
# except ZeroDivisionError as e:
#     print('except:',e)
# else:
#     print('no error')
# finally:
#     print('finally...')
# print('END')

'''logging'''
# import logging
# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
# main()
# print('END')

# try:
#  10 / 0
# except ZeroDivisionError:
#  raise ValueError('input error!')

'''assert'''
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
# def main():
#     foo('0')
# main()

'''logging'''
# import logging
# logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n=%d'%n)
# print(10/n)

'''pdb.set_trace()'''
import pdb
s='0'
n=int(s)
pdb.set_trace()
print(10/n)