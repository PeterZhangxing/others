#！/usr/bin/python3.5

# products_list = [
#     ('telephone',2000),
#     ('computer',12000),
#     ('bicycle',20000),
#     ('television',4500),
#     ('kindle',1450),
# ]
# shopping_list = []
# salary = input("please input how much money you obtain: ")
# if salary.isdigit():
#     salary = int(salary)
#     while True:
#         for index,item in enumerate(products_list):
#             print(index,item)
#         user_choice = input("Please input the series number of the item you want to buy:")
#         if user_choice.isdigit():
#             user_choice = int(user_choice)
#             if user_choice < len(products_list) and user_choice >= 0:
#                 p_item = products_list[user_choice]
#                 if p_item[1] <= salary:
#                     shopping_list.append(p_item)
#                     salary = salary - p_item[1]
#                     print("\033[42;1m%s\033[0m is added to your cart and you have \033[31;1m%s\033[0m left." %(p_item[0],salary))
#                 else:
#                     print("You do not have enough money left to buy anything!")
#             else:
#                 print("You haven't input a valid series number of item!")
#         elif user_choice == "q" or user_choice == "exit":
#             print('------your shopping list------')
#             for p in shopping_list:
#                 print(p)
#             print("The money you have now:",salary)
#             exit()
#         else:
#             print("invalid option,please retry.")

# test_str = 'this is'
#
# print(test_str.swapcase())
#
# print(test_str.capitalize())
#
# print(test_str.title())
#
# print(test_str[3::-1])
#
# for i in range(10,0,-2):
#     print(i)

# test_li = [1,2,3,4,5]
#
# # 指明要删除的元素的下标
# # test_li.pop(1)
# # print(test_li)
#
# # 指明要删除的元素
# test_li.remove(1)
# print(test_li)

# dc = {'t':123,'p':234}

# 从字典中弹出某个建对应的值，如果没有这个键，设置默认返回的值
# res = dc.pop('t','no such key')
# res1 = dc.pop('h','no such key')
# print(dc,'\n',res,'\n',res1)

# 获取字典中某键对应的值
# res = dc['t'] # 没有键，直接报错退出
# res1 = dc.get('t','no such key') # 没有键时，不会报错，返回none
# print(dc,'\n',res,'\n',res1)


# test_str_en = 'test'
# test_str_ch = '测试'
#
# # 将字符串用utf8格式，编码为二进制数
# test_str_en_b = test_str_en.encode('utf-8')
# test_str_ch_b = test_str_ch.encode('utf-8')
#
# print(test_str_ch_b)
# print(test_str_en_b)
# # b'\xe6\xb5\x8b\xe8\xaf\x95'
# # b'test'
#
# # 用utf8编码格式，将二进制代码翻译为字符串
# test_str_en_d = test_str_en_b.decode('utf-8')
# test_str_ch_d = test_str_ch_b.decode('utf-8')
#
# print(test_str_ch_d)
# print(test_str_en_d)
# # 测试
# # test

# s = set('hello')
# t = set([123,'2','h','o'])
#
# print(s.symmetric_difference(t))


# 直接赋值，两个变量指向同一个内存地址
# l1 = [1,2,3]
# l2 = l1
# print(l1,l2)
# print(id(l1),id(l2))
# l2.append('a')
# print(l1,l2)
# # [1, 2, 3] [1, 2, 3]
# # 2216889388552 2216889388552
# # [1, 2, 3, 'a'] [1, 2, 3, 'a']


# 浅复制，仅复制列表的第一维元素到新内存中，二维以上的元素仍然共享同样的内存，并没有复制多份
# l1 = [1,2,3]
# l2 = l1.copy()
# print(l1,l2)
# print(id(l1),id(l2))
# l2.append('a')
# print(l1,l2)
# [1, 2, 3] [1, 2, 3]
# 1368622140936 1368622140872
# [1, 2, 3] [1, 2, 3, 'a']


# 浅复制，仅复制列表的第一维元素到新内存中，二维以上的元素仍然共享同样的内存，并没有复制多份
# l1 = [1,2,[4,5,6],3]
# l2 = l1.copy()
#
# print(l1,id(l1))
# print(l2,id(l2))
# # [1, 2, [4, 5, 6], 3] 1624710811080
# # [1, 2, [4, 5, 6], 3] 1624709004680
#
# l1.append('a')
# print(l1,l2)
# # [1, 2, [4, 5, 6], 3, 'a'] [1, 2, [4, 5, 6], 3]
#
# l1[2].append('a')
# print(l1,l2)
# print(id(l1[2]))
# print(id(l2[2]))
# # [1, 2, [4, 5, 6, 'a'], 3, 'a'] [1, 2, [4, 5, 6, 'a'], 3]
# # 1624710811144
# # 1624710811144


# 深复制，列表的整个内容都被复制了多份，而不仅是第一维元素
# import copy
#
# l1 = [1,2,[4,5,6],3]
# l2 = copy.deepcopy(l1)
# print(l1,id(l1))
# print(l2,id(l2))
# # [1, 2, [4, 5, 6], 3] 2610551885192
# # [1, 2, [4, 5, 6], 3] 2610551913992
#
# l1[2].append('a')
# print(l1,l2)
# # [1, 2, [4, 5, 6, 'a'], 3] [1, 2, [4, 5, 6], 3]


# 切片赋值相当于直接赋值
# l1 = [1,[1],2,3,4]
# l2 = l1[:]
# l1[1].append('a')
#
# print(l1,id(l1))
# print(l2,id(l2))
# print(l1[1] is l2[1])
# # [1, [1, 'a'], 2, 3, 4] 1917694545352
# # [1, [1, 'a'], 2, 3, 4] 1917692738952
# # True

# import os,sys
#
# file_state = os.stat('QR.png')
# print(type(file_state.st_size))
#
# # os.path.dirname(__file__)
# sys.path.append(os.path.dirname(__file__))
# print(sys.path)

# li = [1,2,3,]
# # enumerate函数的第二个参数为自己设定列表的序列号的起始值，默认为0
# for i,v in enumerate(li,2):
#     print(i,':',v)
# # 2 : 1
# # 3 : 2
# # 4 : 3

# import os
#
# print(os.cpu_count())


# 正则表达式的非非贪婪模式
# import re
#
# c_mode1 = re.compile(r"a(.*)a\(\)")
# c_mode2 = re.compile(r"a(.*?)a")
#
# test_string = r"activeactivea()"
# res = re.search(c_mode1,test_string)
# print(res.group())
# print(res.group(1))
#
# res1 = re.search(c_mode2,test_string)
# print(res1.group())
# print(res1.group(1))

# 多重装饰器
# def outer2(func):
#     def inner(a,b):
#         print('in inner2')
#         return func(a,b)
#     return inner
#
# def outer1(func):
#     def inner(a,b):
#         print('in inner1')
#         return func(a,b)
#     return inner
#
# @outer2
# @outer1
# def test_dec(a,b):
#     return a+b
#
# res = test_dec(10,11)
# print(res)

# 带参数的装饰器函数
# def deco(ab):
#     def outer(func):
#         def inner(a,b):
#             print('begin of inner '+ab)
#             res = func(a,b)
#             print('end of inner '+ab)
#             return res
#         return inner
#     return outer
#
# @deco("in deco")
# def test_dec(a,b):
#     return a+b
#
# res = test_dec(10,11)
# print(res)


######## 多维数组展开为一维
# def bopi(li):
#     res_li = []
#     for i in li:
#         if isinstance(i,list):
#             for j in bopi(i):
#                 res_li.append(j)
#         else:
#             res_li.append(i)
#     return res_li
#
# test_li = [1,2,[1,[45,21]],[4,[33,[34,[43,78,1,4]]]]]
#
# res = bopi(test_li)
# print(res)

# names = ('tom','jerry','bilibili','micky')
# # firstn,*_,lastn = names
# # print(firstn,lastn)
#
# x_li = (1 if len(i)>3 else 2 for i in names)
#
# for i in x_li:
#     print(i)

# from selenium import webdriver
#
# mydriver = webdriver.Chrome()
# mydriver.get('https://www.baidu.com')
# print(mydriver.page_source)
# mydriver.close()

import pandas as pd
import numpy as np


# index_li = [chr(i+65) for i in range(12)]
# print(index_li)
# t1 = pd.Series(np.arange(12),index=index_li)
# print(t1)

# data_li = [{"name":"zx","age":100,"phone":10086},
#            {"name":"hejia","age":98},
#            {"name":"nuniu","age":32,"phone":19089},
#            {"name":"nuniu","age":34,"phone":34598},
#            {"name":"nuniu","phone":98763},]
#
# t2 = pd.DataFrame(data_li)
# print(t2)
#
# t2["age"].fillna(t2["age"].mean(),inplace=True)
# # print(t2["age"].mean())
#
# print(t2)

# print(np.random.choice(range(1,11),5))


# class MyType(type):
#
#     def __init__(self,*args,**kwargs):
#         '''
#         在构建以此类为源类的类时，自动调用此方法
#         :param args:
#         :param kwargs:
#         '''
#         print('in metaclass init')
#         super(MyType,self).__init__(*args,**kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         '''
#         实例化以此类为源类的类的对象时，调用此方法
#         :param args:
#         :param kwargs:
#         :return:
#         '''
#         print('in metaclass call')
#
#         obj = cls.__new__(cls,*args, **kwargs)
#
#         cls.__init__(obj, *args, **kwargs)
#
#         return obj
#
#
# class TestMeta(object,metaclass=MyType):
#
#     def __init__(self, *args, **kwargs):
#         print('in testmeta init')
#         self.name = args[0]
#
#     def __new__(cls, *args, **kwargs):
#         print('in testmeta new')
#         # return super(TestMeta,cls).__new__(cls) # 调用object的__new__方法生产新的对象
#         return object.__new__(cls)
#
#     def show_name(self):
#         return self.name
#
#
# testmeta_obj = TestMeta('zx')
# print(type(testmeta_obj))
# print(testmeta_obj.show_name())
# '''
# in metaclass init
# in metaclass call
# in testmeta new
# in testmeta init
# <class '__main__.TestMeta'>
# zx
# '''
# print(TestMeta.__dict__)
# print(dir(TestMeta))

# class Mytype(type):
#
#     def __init__(self,*args,**kwargs):
#         super(Mytype,self).__init__(*args,**kwargs)
#
# class FFoo(object):
#     age = 100
#
# class MFoo(object):
#     gender = "Male"
#
# def with_metaclass(*args):
#     '''
#     使用另一种创建类的方式，创建一个继承任意个类的子类
#     :param args:
#     :return:
#     '''
#     # print(args) # (<class '__main__.MFoo'>, <class '__main__.FFoo'>)
#     Base = Mytype("Base",args,{'name':'zx'}) # 使用源类创建类
#     return Base
#
# class Foo(with_metaclass(MFoo,FFoo)):
#     pass
#
# foo = Foo()
# print(foo.name)
# print(foo.age)
# print(foo.gender)
'''
zx
100
Male
'''

from pandas import DataFrame

# col = pd.MultiIndex.from_product([['midterm','finalterm'],['math','chinese','english']])
# ind = pd.MultiIndex.from_product([['class4',],['zhs','lisi','hj']])
#
# df = DataFrame(data=np.random.randint(59,100,size=(3,6)),index=ind,columns=col)
#
# print(df)
#
# print(df['midterm'].loc['class4'].loc['lisi']['math'])
#
# print("*"*50)
# df['midterm'].loc['class4'].loc['lisi']['math'] = 88
# print(df)
#
# print("*"*50)
# df['midterm'].loc['class4'].loc['lisi']['math'] = np.NaN
# print(df)
'''
            midterm                 finalterm                
               math chinese english      math chinese english
class4 zhs       99      94      95        66      77      80
       lisi      80      85      92        82      89      74
       hj        82      67      62        82      99      88
80
**************************************************
            midterm                 finalterm                
               math chinese english      math chinese english
class4 zhs       99      94      95        66      77      80
       lisi      80      85      92        82      89      74
       hj        82      67      62        82      99      88
**************************************************
            midterm                 finalterm                
               math chinese english      math chinese english
class4 zhs       99      94      95        66      77      80
       lisi      80      85      92        82      89      74
       hj        82      67      62        82      99      88
'''

# df1 = DataFrame(data=np.random.randint(59,100,size=(3,4)),
#                 index=['zx','hj','hh'],columns=['math','chinese','english','physiology'])
#
# # print(df1)
#
# df1['math'].loc['hj'] = np.nan

# print(df1)
'''
    math  chinese  english  physiology
zx    67       78       73          60
hj    92       88       72          96
hh    75       89       92          81
    math  chinese  english  physiology
zx  67.0       78       73          60
hj   NaN       88       72          96
hh  75.0       89       92          81
'''

# print(np.random.permutation([1,2,3,4]))
# [2 1 3 4]
# print(np.random.permutation(4))
# [2 3 1 0]

# 随机排序dataframe中的行数据
# df2 = df1.take(np.random.permutation(df1.shape[0]),axis=0)
# print(df2)


# import yaml
#
# # 新版本要求必须指定loader，否则会出现警告
# from yaml.loader import SafeLoader
#
# def yaml_parser(yml_filename):
#     '''
#     load yaml file and return
#     :param yml_filename:
#     :return:
#     '''
#     #yml_filename = "%s/%s.yml" % (settings.StateFileBaseDir,yml_filename)
#     try:
#         # 打开并读取一个yml格式的文件
#         yaml_file = open(yml_filename,'r')
#
#         # 解析文件，返回的内容是一个列表嵌套字典的数据格式
#         data = yaml.load(yaml_file,Loader=SafeLoader)
#
#         return data
#     except Exception as e:
#         print(str(e))
#
# data = yaml_parser('test.yml')
# print(data)
'''
- hosts: sample_group_name
  tasks:
  - name: just an uname
    command: uname -a

[{'hosts': 'sample_group_name', 'tasks': [{'name': 'just an uname', 'command': 'uname -a'}]}]
'''

# import cv2
# import os
#
# def getpic():
#     cap = cv2.VideoCapture(0)
#     ret,frame = cap.read()
#     # print(ret) # 是否成功获取照片
#     if not ret:
#         res = None
#     else:
#         cv2.imwrite('pic.jpg',frame)
#         res = os.path.abspath('pic.jpg')
#     # res = os.path.join(os.getcwd()+'\pic.jpg')
#     return res
#
# res = getpic()
# print(res)

# class A(object):
#     def __init__(self):
#         print("A")
#
# class ASon1(A):
#     def __init__(self):
#         super().__init__()
#         print("ASon1")
#
# class ASon2(A):
#     def __init__(self):
#         super().__init__()
#         print("ASon2")
#
# class Child(ASon1,ASon2):
#     def __init__(self):
#         super().__init__()
#         print("Child")
#
# child = Child()
# print(Child.__mro__)
'''
A
ASon2
ASon1
Child
(<class '__main__.Child'>, <class '__main__.ASon1'>, 
<class '__main__.ASon2'>, 
<class '__main__.A'>, <class 'object'>)
'''

# class A(object):
#     def __init__(self):
#         print("A")
#
# class ASon1(A):
#     def __init__(self):
#         super().__init__()
#         print("ASon1")
#
# class ASon2(A):
#     def __init__(self):
#         super().__init__()
#         print("ASon2")
#
# class Child(ASon1,ASon2):
#     def __init__(self):
#         super(ASon2,self).__init__()
#         print("Child")
#
# child = Child()
# print(Child.__mro__)

# mystr = 'this is a test'
# mynew = mystr.replace('this','that')
# print(mynew,mystr)

# for i in range(1,10):
#     for j in range(i,10):
#         print("%s*%s=%s"%(i,j,i*j),end=';')
#     print()

# def myfib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     a,b = 0,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
#
# for i in range(1,10):
#     res = myfib(i)
#     print(res,end=' ')


# def myfib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     else:
#         return myfib(n-1) + myfib(n-2)
#
# def buid_fib_li(n):
#     fib_li = []
#     for i in range(1,n+1):
#         fib_li.append(myfib(i))
#     return fib_li
#
# print(myfib(9))
# print(buid_fib_li(9))

# 可迭代对象 __iter__
# class TestIter(object):
#
#     def __init__(self):
#         self.names = []
#         self.num = 0
#
#     def __iter__(self):
#         return TestNext()
#
# class TestNext(object):
#
#     def __init__(self):
#         self.names = ['zx','hj','xr']
#         self.num = 0
#
#     def __next__(self):
#         self.total = len(self.names)
#         if self.num < self.total:
#             res = self.names[self.num]
#             self.num += 1
#             return res
#         else:
#             raise StopIteration
#
# my_test = TestIter()
# for name in my_test:
#     print(name)

# 迭代器 __iter__,__next__
import time

# class TestIter(object):
#
#     def __init__(self):
#         self.names = []
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#     def add_name(self,newname):
#         self.names.append(newname)
#
#     def __next__(self):
#         self.toallen = len(self.names)
#
#         time.sleep(0.5)
#         if self.num < self.toallen:
#             res = self.names[self.num]
#             self.num += 1
#             return res
#         else:
#             raise StopIteration # 捕获到该异常，退出for循环
#
# testiter = TestIter()
#
# testiter.add_name('zx')
# testiter.add_name('hj')
# testiter.add_name('lb')
#
# # 获取__iter__方法的返回值，循环一次，调用一次这个对象的__next__方法
# for obj in testiter:
#     print(obj)

# class MyFib(object):
#
#     def __init__(self,total_num):
#         self.a = 0
#         self.b = 1
#
#         self.num = 1
#         self.total_num = total_num
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num <= self.total_num:
#             if self.num == 1:
#                 self.num += 1
#                 return 0
#             self.a,self.b = self.b,self.a+self.b
#             self.num += 1
#             return self.a
#         else:
#             raise StopIteration
#
# myfib = MyFib(100)
# # print(next(myfib))
# # print(next(myfib))
# # print(next(myfib))
# # print(next(myfib))
# # print(next(myfib))
# for obj in myfib:
#     print(obj)

# 生成器(特殊的迭代器) yield
# def testyield(num):
#     for i in range(num):
#         res = yield i
#         print('this is %s'%res)
#
# yobj = testyield(10)
# print(next(yobj))
# # print(next(yobj))
# # print(next(yobj))
# # print(next(yobj))
# yobj.send("hahaha")

# gevent实现协程
# import gevent
# from gevent import monkey
# import requests
#
# monkey.patch_all()
#
# def get_response(url):
#     response = requests.get(url=url)
#     return url,len(response.text)
#
# url_li = [
#     'http://www.xiaohuar.com/',
#     'https://www.baidu.com/',
#     'http://dig.chouti.com/',
#     'https://www.bilibili.com/',
#     'https://www.taobao.com/'
# ]
#
# g_li = list()
# for url in url_li:
#     g_li.append(gevent.spawn(get_response,url))
#
# gevent.joinall(g_li)
#
# for g in g_li:
#     print(g.value)

# from threading import Timer
# import threading
#
# def func():
#     print(threading.get_ident())
#
# while True:
#     # 每隔3秒开启一个新的子线程运行定义的代码
#     tt = Timer(3,func)
#     tt.start()
#     tt.join()

# from threading import Thread
# import threading
# import time
#
# def func1():
#     time.sleep(5)
#     print("in normal thread:",threading.get_ident())
#
# def func2():
#     while True:
#         time.sleep(1)
#         print('***in daemon thread:',threading.get_ident())
#
# td = Thread(target=func2)
# td.daemon = True # 设置一个线程为守护线程
# td.start()
#
# t_li = []
# for i in range(10):
#     t = Thread(target=func1)
#     t_li.append(t)
#     t.start()
# # 保证所有子线程运行结束，才执行后面主线程的代码
# for t in t_li:t.join()
#
# print('main thread')

# import threading
# import time
#
# """重新定义带返回值的线程类"""
# class MyThread(threading.Thread):
#     def __init__(self, func, args=()):
#         super(MyThread, self).__init__()
#         self.func = func
#         self.args = args
#
#     def run(self):
#         self.result = self.func(*self.args)
#
#     def get_result(self):
#         try:
#             return self.result
#         except Exception:
#             return None
#
# """测试函数，计算两个数之和"""
# def fun(a, b):
#     time.sleep(1)
#     return a + b
#
# li = []
# for i in range(4):
#     t = MyThread(fun, args=(i, i + 1))
#     li.append(t)
#     t.start()
#
# [t.join() for t in li]
# res_li = [t.get_result() for t in li]
# print(res_li)

# from multiprocessing import Pool
# import time
#
# def func(n):
#     time.sleep(0.3)
#     return n+1
#
# pool = Pool(4)
# # # 使用map的方式获取各个子进程的返回结果
# res = pool.map(func,[i for i in range(20)])
# print(res)
#
# res_li = []
# for i in range(20):
#     res = pool.apply_async(func,args=(i,))
#     res_li.append(res)
# # 使用apply_async的方式获取每个子进程返回的结果
# res_dli = [res.get() for res in res_li]
# print(res_dli)

# import re
#
# mycontent = "<h1><p>this is a test</p></h1>"
# recontent1 = r'<(\w+)><(\w+)>(.*?)</\2></\1>'
# recom = re.compile(recontent1)
#
# res = recom.match(mycontent)
# # res1 = re.match(recontent1,mycontent)
#
# print(res.group())
# print(res.group(3))
# # print(res1)

# content = """
# ewqeqwewqe qweqwe ewqe
# this is a test
# dasdsad dasda dsadas
# hhahah hahha haha
# """
#
# res = content.splitlines(keepends=True)
# print(res)

# f_li = [ lambda i:i+100 for i in range(10) ]
# for f in f_li:
#     print(f(1))

# info_dict_li = [{'name':'zx','age':100},{'name':'hj','age':20},{'name':'hh','age':120}]
# res = sorted(info_dict_li,key=lambda mydict:mydict['age'])
# print(res)

# def outer(func):
#     print('in outer function')
#     print(func) # <function myfunc at 0x0000029D51F1B6A8>
#     def inner(*args,**kwargs):
#         print('before func')
#         print(*args,**kwargs)
#         res = func(*args,**kwargs)
#         print('after func')
#         return res
#     return inner
#
# @outer
# def myfunc(i,a=32,b=120,c=100):
#     return "in myfunc %s%s%s%s"%(i,a,b,c)
#
# print(myfunc(1,32,120,100))


# def pass_param(a,b):
#     def outer(func):
#         def inner(*args, **kwargs):
#             print('before func')
#             print('a+b=',a+b)
#             print(*args, **kwargs)
#             res = func(*args, **kwargs)
#             print('after func')
#             return res
#         return inner
#     return outer
#
# @pass_param(10,100)
# def myfunc(i,a=32,b=120,c=100):
#     return "in myfunc %s%s%s%s"%(i,a,b,c)
#
# print(myfunc(1,32,120,100))


# def outer1(func):
#     print('in outer1 function')
#     def inner(*args,**kwargs):
#         print('in inner1')
#         res = func(*args,**kwargs)
#         return res
#     return inner
#
# def outer2(func):
#     print('in outer2 function')
#     def inner(*args,**kwargs):
#         print('in inner2')
#         res = func(*args,**kwargs)
#         return res
#     return inner
#
# @outer2
# @outer1
# def myfunc(i,a=32,b=120,c=100):
#     return "in myfunc %s%s%s%s"%(i,a,b,c)
#
# print(myfunc(1,32,120,100))
#
# '''
# in outer1 function
# in outer2 function
# in inner2
# in inner1
# in myfunc 132120100
# '''

# class MyDec(object):
#
#     def __init__(self,func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('before func')
#         res = self.func(*args, **kwargs)
#         print('after func')
#         return res
#
# @MyDec # myfunc = MyDec(myfunc)
# def myfunc(a,b):
#     return a + b
#
# print(myfunc(1,2))

# mmm = 'abcd'
# print(globals())

# import copy
#
# a = [1,2,3]
# b = [4,5,6]
# li = [a,b]
#
# norm_cp = copy.copy(li)
# norm_cp[0][0] = 100
# print(a)
#
# norm_cp = copy.deepcopy(li)
# norm_cp[0][0] = 100
# print(a)

import re

# tag_str ='''
# <img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" \n src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
# '''
#
# res1 = re.search(r'https://.*\.jpg',tag_str,re.S)
# print(res1.group())
#
# res2 = re.search(r'https://.*?\.jpg',tag_str)
# print(res2.group())

# ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
# print(ret.group())

# ret = re.finditer('\d', 'ds3sy4784a')
# for i in ret:
#     print(i.group())

# ret = re.subn('\d', 'H', 'eva3egon4yuan4')
# #将数字替换成'H'，返回元组(替换的结果,替换了多少次)
# print(ret)

# li1 = ['a','b','c']
# li2 = ['A','B','C','C']
#
# my_dict = {}
# for i in li1:
#     for j in li2:
#         my_dict.setdefault(i,{})
#         my_dict[i].setdefault(j,0)
#         my_dict[i][j] += 1
#
# print(my_dict)
#
# dt = dict.fromkeys(li2)
# print(dt)

# import time

# i = 2521
# start_time = time.time()
# while True:
#     k = 1
#     for j in range(2,21):
#         res,divres = divmod(i,j)
#         if divres != 0:
#             break
#         else:
#             k += 1
#     if k == 20:
#         end_time = time.time()
#         print('spend:%sM'%str((end_time-start_time)//60))
#         exit(i) # 232792560
#     i += 1

# i = 1
# start_time = time.time()
# while True:
#     tag = True
#     for j in range(2,21):
#         res,divres = divmod(i,j)
#         if divres != 0:
#             tag = False
#             break
#     if tag:
#         end_time = time.time()
#         print('spend:%sM'%str((end_time-start_time)//60))
#         exit(i) # 232792560
#     i += 1
#
# total = 1
# for i in range(1,21):
#     total *= i
# print(total)

############# 求能整除1到某个正整数范围内的，所有整数的最小正整数 #############
# import time
#
# def cal_run_time(func):
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         res = func(*args,**kwargs)
#         end_time = time.time()
#         print(end_time-start_time)
#         return res
#     return inner
#
# def juge_num(num):
#     for i in range(2,num//2+1):
#         if num % i == 0:
#             return False
#     else:
#         return True
#
# def get_num_ele(num):
#     ele_li = []
#     if juge_num(num):
#         return [1,num]
#     while True:
#         if juge_num(num) and num != 1:
#             ele_li.append(num)
#             break
#         for i in range(2,num//2+1):
#             if num % i == 0 and juge_num(i):
#                 ele_li.append(i)
#                 num = num//i
#                 break
#
#     return sorted(ele_li)
#
# def found_all_sushu(num):
#     sushu_li = []
#     for i in range(2,num+1):
#         if juge_num(i):
#             sushu_li.append(i)
#     return sushu_li
#
# def get_sushumul_res(num):
#     li = found_all_sushu(num)
#     res = 1
#     for i in li:
#         res *= i
#     return res
#
# def find_unmod(num):
#     mul_res = get_sushumul_res(num)
#     unmod_li = []
#     for i in range(2,num+1):
#         if mul_res % i != 0:
#             unmod_li.append(i)
#     return unmod_li
#
# def get_mini_num(num):
#     mydict = {}
#     unmod_li = find_unmod(num)
#     for i in unmod_li:
#         tmp_dict = {}
#         for j in get_num_ele(i):
#             tmp_dict.setdefault(j,0)
#             tmp_dict[j] += 1
#         mydict[i] = tmp_dict
#     # print(mydict)
#
#     count_dict = {}
#     for k,v in mydict.items():
#         for key,value in v.items():
#             count_dict.setdefault(key,value)
#             if count_dict[key] < value:
#                 count_dict[key] = value
#     # print(count_dict)
#
#     extra_mul_num = 1
#     for k,v in count_dict.items():
#         extra_mul_num *= k**(v-1)
#
#     return extra_mul_num * get_sushumul_res(num)
#
# @cal_run_time
# def main(num):
#     res = get_mini_num(num)
#     return res
#
# res = main(40)
# print(res) # 232792560 9699690

# li = [1,2,2,3,4,4,4,5,1,1,1,5,2,3]
# mydict = {'name':'zx','age':32,'nickname':'ppp'}
#
# li.pop(2)
# li.pop()
#
# print(li.__len__())
# print(li.index(1))
# print(li.count(1))
# print(li)
#
# li.reverse()
# print(li)
# li_r = list(reversed(li))
# print(li_r)
#
# mydict.pop('nickname')
# print(mydict)

################## 列表去重 ##################
# li = [1,2,2,2,2,3,4,4,4,5,1,1,1,5,2,3]

# new_li = []
# for i in li:
#     if i not in new_li:
#         new_li.append(i)
# print(new_li)

# for i,v in enumerate(li):
#     # print(i)
#     j = i + 1
#     while j < len(li):
#         if li[i] == li[j]:
#             del li[j]
#             continue
#         j += 1
# print(li)
#
# for i in range(len(li)):
#     j = i + 1
#     while j < len(li):
#         if li[i] == li[j]:
#             del li[j]
#             continue
#         j += 1
# print(li)

# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         try:
#             if li[i] == li[j]:
#                 del li[j]
#         except:
#             break
# print(li)

# for i,v in enumerate(li):
#     # print(i)
#     for j, k in enumerate(li,start=i+1):
#         try:
#             if li[i] == li[j]:
#                 del li[j]
#         except:
#             break
# print(li)


# def test_arg(li):
#     # new_li = li[:]
#     # new_li = copy.copy(li)
#     new_li = copy.deepcopy(li)
#     new_li.append(3)
#     return new_li
#
# myli = [1,2]
#
#
# import copy
#
# res = test_arg(myli)
#
# print(myli)
# print(res)
#
# copy.copy()
# copy.deepcopy()

# import copy
#
# i = {'name':'zx','age':22}
# j = {'name':'hj','age':23}
#
# v = {'name':'bj','age':32}
# k = {'name':'lj','age':33}
#
# a_li = [i,j]
# b_li = [v,k]
#
# # a = a_li
# # b = b_li
# # a = copy.copy(a_li)
# # b = copy.copy(b_li)
#
# a = copy.deepcopy(a_li)
# b = copy.deepcopy(b_li)
#
# c_li = [a,b]
#
# # c_li[0].append(9)
# c_li[0][0]['age'] = 100
# print(a_li)
# print(c_li)

# a = 1
# b = a
#
# b = 2
# # b.append(2)
# print(a,b)

print("{0:.02f} is a {1:d} {0:.03f} {2}".format(1.2312,100,'haha'),end='')
print("\r{mf:.02f} is a {md:d} {mf:.03f} {ms}".format(mf=1.231,md=120,ms='hopi'))
print("{mf} is a {md} {mf} {ms}".format(mf=1.231,md=120,ms='hopi'))
print('name\tage\tgender\tschool')
print('zx','\t',100,'\t','male','\t','JLU')