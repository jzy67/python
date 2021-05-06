# 常用运算符
# / % ** //
# == != 
# = *= += //=
# and or not
name=input("your name:").strip()
age=input("age:")
if age.isdigit():
    age=int(age)
else:
    print("错误输入！")
    exit()
print(type(age))
hobbie=input("your hobbie:")
job=input("your job:")
msg=f'''
name={name}
age={age},still young in {30-(age)} years you will be 30
hobbie={hobbie}
job={job}
'''
print(msg)