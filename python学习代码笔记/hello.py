#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 'a test module'

# _author_='Jiang'

# import sys
# def test():
#     args=sys.argv
#     if len(args)==1:
#         print('hello world')
#     elif len(args)==2:
#         print("hello,%s"%args[1])
#     else:
#         print('too many arguments')
# if __name__=='_main_':
#     test()
from PIL import Image
im=Image.open("assignment2.png")
print(im.format,im.size,im.mode)
im=im.convert('RGB')
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')