# class Student(object):
#     def __init__(self,name,score):
#         self.__name=name
#         self.__score=score
#     def print_score(self):
#         print('%s: %s'%(self.__name,self.__score))
#     def get_grade(self):
#         if self.__score>=90:
#             return 'A'
#         elif self.__score>=60:
#             return 'B'
#         else:
#             return 'C'
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#     def set_score(self,score):
#         self.__score=score

# bart=Student('Bart',59)
# bart.print_score()
# bart.get_grade()

# class Student(object):
#     __slots__=('name','age','set_age')#只对当前类有限制，对子累不影响
#     pass
# s=Student()
# s.name='michael'
# print(s.name)
# def set_age(self,age):
#     self.age=age
# from types import MethodType
# s.set_age=MethodType(set_age,s)#对另一个实例不起作用，使用Student.set_age=MethodType(set_age,Student) s2=Student()s2.set_age(25)
# s.set_age(25)
# print(s.age)
# class GraduateStudent(Student):
#     pass
# g=GraduateStudent()
# g.score=99
# print(g.score)

'''@property的使用'''
# class Student(object):
#     def get_score(self):
#         return self.score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer!')
#         if value>100 or value<0:
#             raise ValueError('score must between 0~100!')
#         self.score=value
# s=Student()
# s.set_score(99)      
# class Student(object):
#     @property#只读
#     def score(self):
#         return self._score
#     @score.setter#只写
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# s=Student()
# s.score=60
#s.score=900

'''练习'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        self._width=width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height=height
    @property
    def resolution(self):
        return self._width*self._height
s=Screen()
s.width=1024
s.height=768
print(s.resolution)
assert s.resolution==786432,'1024*768=%d?' % s.resolution