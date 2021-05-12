import os
# print(os.name,'\n',os.environ,'\n',os.environ.get('PATH'))
'''实现 dir -l 输出的程序'''
gen=[x for x in os.listdir('D:/')]
print(gen)
'''在当前目录以及当前目录的所有子目录下查找
文件名包含指定字符串的文件，并打印出相对路径'''
# def gci(filepath):
#     files=os.listdir(filepath)
#     for file in files:
#         path=os.path.join(filepath,file)
#         if os.path.isdir(path):
#             gci(path)
#         elif os.path.splitext(path)[1]=='.py':
#             print(path)
# gci('.')
