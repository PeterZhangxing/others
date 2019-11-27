#!/usr/bin/python3.5

class school(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []
    def enroll(self,stu_obj):
        self.students.append(stu_obj)
        print("033[31m%s erolled!033[0m"%(stu_obj.name))
    def hire(self,staff_obj):
        self.staffs.append(staff_obj)
        print("033[31m%s are hired!033[0m"%(staff_obj.name))

class schoolmember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class teacher(schoolmember):
    def __init__(self,name,age,sex,salary,course):
        super(teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        -------- info of %s --------
        Name: %s
        Age: %s
        Sex: %s
        Salary: %s
        Course: %s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching %s!"%(self.name))
    def get_paied(self,amount):
        print("%s are paied %s for salary!"%(self.name,amount))

class student(schoolmember):
    def __init__(self,name,age,sex,stuid,grade):
        super(student,self).__init__(name,age,sex)
        self.stuid = stuid
        self.grade = grade
    def tell(self):
        print('''
        -------- info of %s --------
        Name: %s
        Age: %s
        Sex: %s
        Stuid: %s
        Grade: %s
        '''%(self.name,self.name,self.age,self.sex,self.stuid,self.grade))
    def pay_tuition(self,amount):
        print("%s has paid %s for tuition"%(self.name,amount))

my_high_school = school("The Eighth High School Of KunMing","kunming yunnan china")
t1 = teacher("linlin","56","female","180000","english")
s1 = student("xuran","37","female","010250440779","5th")
t2 = teacher("laoluo","66","male","190000","french")
s2 = student("chengxi","36","female","010250440789","5th")

my_high_school.enroll(s1)
my_high_school.hire(t1)
my_high_school.enroll(s2)
my_high_school.hire(t2)

print("all the students we are having are under below:")
for i in my_high_school.students:
    print(i.tell())
print("-------------------end-------------------------")

print("\r\n")

print("all the staffs we are having are under below:")
for i in my_high_school.staffs:
    print(i.tell())
print("-------------------end-------------------------")

for i in my_high_school.students:
    i.pay_tuition(5000)

print("\r\n")

for i in my_high_school.staffs:
    i.get_paied(5000)