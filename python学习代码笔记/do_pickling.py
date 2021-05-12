# import pickle
# d=dict(name='Bob',age=20,score=88)
# # print(pickle.dumps(d))
# # f=open('D:/dump.txt','wb')
# # pickle.dump(d,f)
# # f.close()
# f=open('D:/dump.txt','rb')
# d=pickle.load(f)
# f.close()
# print(d)

'''json'''
# import json
# d=dict(name='Bob',age=20,score=88)
# # print(json.dumps(d))
# f=open('D:/dump.txt','w')
# json.dump(d,f)
# f.close()
# f=open('D:/dump.txt','r')
# d=json.load(f)
# f.close()
# print(d)

import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s=Student('Bob',20,80)
def student2dict(std):
    return {'name':std.name,'age':std.age,'score':std.score}
# print(json.dumps(s,default=student2dict))
f=open('D:/dump.txt','w')
json.dump(s,f,default=student2dict)
f.close()
def dict2student(dict):
    return Student(dict['name'],dict['age'],dict['score'])
f=open('D:/dump.txt','r')
s=json.load(f,object_hook=dict2student)
f.close()
print(s)