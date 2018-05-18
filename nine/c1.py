# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类 对象
from c3 import Human


class Student(Human):
    def __init__(self, school, name, age):
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name,age)
        self.school = school
    
    def do_homework(self):
        super(Student, self).do_homework()
        print('english homework')


student1 = Student('人民路小学', '石敢当', 18)
# print(student1.sum)
print(Student.sum)
student1.get_name()
student1.do_homework()
# print(student1.name)
# print(student1.age)

# name = 'qiyue'
# age = 0  ##类变量
# 类变量 实例变量
# 一个班级所有学生的数量
# sum = 0

# def print_file(self):
#     print('name:' + self.name)
#     print('age:'+str(self.age))
# def __init__(self, name, age):
#     # 构造函数
#     # 初始化对象的特征
#     #显胜于隐
#     self.name = name  # 实例变量
#     self.age = age  # 实例变量
#     self.__score = 0
# self.__class__.sum += 1
#     # print('当前学生数量为：')
#     # print(self.__class__.sum)

# def do_english_homework(self):
#     pass

# def marking(self, score):
#     if score < 0:
#         print('不能给人打负分')
#         return
#     self.score = score
#     print(self.name+"本次考试为",self.score)

# @classmethod
# def plus_sum(cls):
#     cls.sum += 1
#     print(cls.sum)

# @staticmethod
# def add(x,y):
#     print('this is a static method')
#     print(Student.sum)
# # def do_homework(self):
# print('homework')


# 行为和特征


# class StudentHomework():
#     homework_name = ''
# student1 = Student('石敢当', 18)
# student1.marking(-1)
# print(student1.__dict__)
# print(student1._Student__score)

# student2 = Student('喜小乐', 18)
# Student.plus_sum()
# student3 = Student('哈哈哈', 18)
# Student.plus_sum()
# student4 = Student('啦啦啦', 18)
# Student.plus_sum()
# print(Student.__dict__)
# student2 = Student()
# student3 = Student()
# print(id(student1))
# print(id(student2))
# print(id(student3))
# print(student1.name)
# print(student2.name)
# print(Student.sum)
