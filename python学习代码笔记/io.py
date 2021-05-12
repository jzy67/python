'''file io'''
# f=open('D:/10.txt','r')
# print(f.read())
# f.close()

# try:
#     f=open('D:/10.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('D:/10.txt','r',encoding='utf-8',errors='ignore') as f:
#     for line in f.readlines():
#         print(line.strip())
# with open('D:/11.txt','w') as f:
#     f.write('jzy')

'''string io'''
# from io import StringIO
# f=StringIO()
# f.write('hello')
# print(f.getvalue())

# from io import StringIO
# f=StringIO('hello\nworld')
# f.read()
# while 1:
#     s=f.readline()
#     if s=='':
#         break
#     print(s.strip())

'''bytesio'''
# from io import BytesIO
# f=BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())

from io import BytesIO
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())



