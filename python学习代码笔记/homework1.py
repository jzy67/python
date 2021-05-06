blackgirl_age=25
print("试试猜年龄")
while True:
    in_age=int(input("请输入数字"))
    if in_age<blackgirl_age:
        print("猜的太小了")
    elif in_age>blackgirl_age:
        print("猜的太大了")
    else:
        print("猜对了")
        exit()
