# import os,sys
#
# # file_state = os.stat('QR.png')
# # print(type(file_state.st_size))
#
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#
# import test_os
#
# test_os.myos_test()


# 函数传参方式测试
# def my_func(a,b,c):
#     print(a,b,c)
#
# def my_func1(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# t_li = [1,2,3]
# t_dict = {'a':1,'b':3,'c':9}
#
# my_func(*t_li)
# # 1 2 3
#
# my_func(**t_dict)
# # 1 3 9
#
# my_func1(*t_li,**t_dict)
# # (1, 2, 3)
# # {'a': 1, 'b': 3, 'c': 9}
#
# my_func1(t_li,t_dict)
# # ([1, 2, 3], {'a': 1, 'b': 3, 'c': 9})
# # {}


# 全局变量和非本地变量的修改
# b = 10
# def outer():
#     global b # 想要修改全局变量，必须先写这一句
#     print("global b : ", b)
#     a = 1
#     b = 1
#     print("outer a :", a)
#     print("global b1 : ",b)
#     def inner():
#         # 想要修改离本层函数最近的外侧函数中的变量，必须先写这一句
#         nonlocal a
#         a += 1
#         print("inner a: ",a)
#     inner()
#     print("outer a1 :",a)
#     return inner
#
# outer()


# 测试变量的类型
# li = []
# mydc = "tyu"
# if type(li) is list and type(mydc) is dict:
#     print('dict or list')
# else:
#     if type(mydc) is int:
#         print('int')
#     elif type(mydc) is str:
#         if mydc.isdigit():
#             print('str digital')
#         elif mydc.isalpha():
#             print('str alp')
#         elif mydc.isalnum():
#             print('alnum')


# 基础装饰器
# def wrapper(func):
#     def inner(*args,**kwargs):
#         print('codes before running func')
#         func_ret = func(*args,**kwargs)
#         print('codes after running func')
#         return func_ret
#     return inner
#
# @wrapper
# def myfunc(a,b):
#     return a if a > b else b
#
# print(myfunc(2,1))


# 使得被装饰器装饰的函数仍然返回自身的属性
# from functools import wraps
#
# def wrapper(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print('codes before running func')
#         func_ret = func(*args,**kwargs)
#         print('codes after running func')
#         return func_ret
#     return inner
#
# @wrapper
# def myfunc(a,b):
#     '''
#     just a test function
#     :param a:
#     :param b:
#     :return:
#     '''
#     return a if a > b else b
#
# # 显示函数的名字
# print(myfunc.__name__)
# # 显示函数的注释信息
# print(myfunc.__doc__)


# print(set([1,2,3]).intersection(set([12,1])))
#
# print(set([1,2,3]).difference(set([12,1])))
#
# for i in range(10,0,-2):
#     print(i)
#
# li = [1,2,3,4,5,6,7]
# print(li[-3:-7:-1])



# 带参数的装饰器

# from functools import wraps
#
# def outter(flag):
#     def wrapper(func):
#         # @wraps
#         def inner(*args,**kwargs):
#             if flag:
#                 print('before %s'%func.__name__)
#                 res = func(*args,**kwargs)
#                 print('after %s'%func.__name__)
#                 return res
#             else:
#                 print('nothing has been changed')
#                 res = func(*args,**kwargs)
#                 return res
#         return inner
#     return wrapper
#
# @outter(True)
# def testfunc(a,b):
#     return a if a > b else b
#
# @outter(True)
# def testfunc1(a,b):
#     return a if a > b else b
#
# bigger_num = testfunc(11,31)
# print(bigger_num)
#
# bigger_num1 = testfunc1(11,3)
# print(bigger_num1)


# 同时使用多个装饰器函数
#
# def wrapper1(func):
#     def inner1(*args,**kwargs):
#         print('before wrapper1 %s'%func.__name__)
#         res = func(*args,**kwargs)
#         print('after wrapper1')
#         return res
#     return inner1
#
# def wrapper2(func):
#     def inner2(*args,**kwargs):
#         print('before wrapper2 %s'%func.__name__)
#         res = func(*args,**kwargs)
#         print('after wrapper2')
#         return res
#     return inner2
#
# def wrapper3(func):
#     def inner3(*args,**kwargs):
#         print('before wrapper3 %s'%func.__name__)
#         res = func(*args,**kwargs)
#         print('after wrapper3')
#         return res
#     return inner3
#
# @wrapper1
# @wrapper2
# @wrapper3
# def testfunc(a,b):
#     return a if a > b else b
#
# b_num = testfunc(1,3)
# print(b_num)


# 生成器的基础语法
# def myiter():
#     for i in range(10):
#         yield i
#
# count = 0
# myiobj = myiter()
# for i in myiobj:
#     if count > 3:
#         break
#     else:
#         print(i)
#         count += 1
#
# print('over 3')
#
# for j in myiobj:
#     print(j)

# a = set(dir(list))
# b = set(dir(int))
# c = a.difference(b)
# # print(a.intersection(b))
# print('__iter__' in c)

# print(chr(99)) # 数字转字符
# print(ord("c")) # 求字符的ASCII码
#
# print(hex(100)) # 求10进制数的16进制值
# print(oct(100)) # 求10进制数的8进制值
# print(bin(100)) # 求10进制数的2进制值


# def generator():
#     print('123')
#     name = yield 'hehe'
#     print(name)
#     yield 'haha'
#
# genobj = generator()
# res1 = genobj.__next__() # 此处执行完生成器函数中的yield，函数就停在了“=”前
# print(res1)
# print('......')
# res2 = genobj.send('pigzhu') # 执行这句就会向等号前的变量赋值，并且执行到下一个yield停止
# print(res2)


# 使用send利用生成器求平均值
# def init_genobj(func):
#     def inner(*args,**kwargs):
#         genobj = func(*args,**kwargs)
#         genobj.__next__()
#         return genobj
#     return inner
#
# @init_genobj
# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum/count
#
# avg_gen = average()
# res = avg_gen.send(10)
# print(res)
# res1 = avg_gen.send(20)
# print(res1)
# res2 = avg_gen.send(30)
# print(res2)
# # 10.0
# # 15.0
# # 20.0

# 在生成器函数中，使用yield from从一个可迭代对象中一次返回一个值
# def mygen():
#     str1 = '123456'
#     str2 = 'abcdef'
#     yield from str1
#     yield from str2
#
# genobj = mygen()
# for i in range(8):
#     obj = genobj.__next__()
#     print(obj)


# 集合生成式
# myset = {i**2 for i in [1,-1,2,3,9] if i%3==0}
# print(myset)
#
# # 字典生成式
# mydict = {i:i*i for i in [1,2,3,4,5,6,7,8,9] if i%2==0 }
# print(mydict)
#
# # 二重列表生成式
# two_d_li = [[1,2,3,4],[-1,-2,-3,-4]]
# li = [i for item in two_d_li for i in item]
# print(li)


# 针对生成器的一些面试题
# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
# print(list(g))
# print(list(g1))
# print(list(g2))
#
#
# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10,5]:
#     g=(add(n,i) for i in g)
#
# # n==1
# # g=(add(n,i) for i in test())
# # n==10
# # g=(add(n,i) for i in (add(n,i) for i in test()))
# # n==5
# # g=(add(5,i) for i in (add(5,i) for i in (add(5,i) for i in test())))
#
# print(list(g))
# # g=(add(5,i) for i in (add(5,i) for i in (5,6,7,8)))
# # g=(add(5,i) for i in (10,11,12,13))
# # g=(15,16,17,18)


# f = open('temp.txt','w',encoding='utf-8')
# print('this is a test',file=f) # 将打印的东西输出到文件
# f.close()

# print('我们的祖国是花园',end='')  #指定输出的结束符,默认是换行
# print('我们的祖国是花园',end='')
# print(1,2,3,4,5,sep='|') #指定输出多个值之间的分隔符，默认是空格
# f = open('file','w')
# print('aaaa',file=f)
# f.close()

# exec('print(123)')
# eval('print(123)')
# print(eval('1+2+3+4')) # 有返回值
# print(exec('1+2+3+4')) # 没有返回值
# exec和eval都可以执行 字符串类型的代码
# eval有返回值  —— 有结果的简单计算
# exec没有返回值   —— 简单流程控制
# eval只能用在你明确知道你要执行的代码是什么


# print(abs(-5)) # 取绝对值
# print(abs(5))
#
# print(divmod(7,2))   # div取商 mod取余
# print(divmod(9,5))   # 除余
#
# print(round(3.14159,3)) # 保留小数点后，三位四舍五入的值
# print(pow(2,3)) # pow幂运算  == 2**3
# print(pow(2,3,3)) # 幂运算之后再取余
#
# ret = sum([1,2,3,4,5,6]) # 求可迭代对象的和
# print(ret)
#
# print(min([1,2,3,4])) # 取最小值
# print(min(1,2,3,-4))
# print(min(1,2,3,-4,key = abs)) # 取绝对值最小的那个数
#
# print(max([1,2,3,4])) # 取最大值
# print(max(1,2,3,4))
# print(max(1,2,3,-4))
# print(max(1,2,3,-4,key = abs)) # 取绝对值最大的那个数


# import time
# for i in range(0,101,4):
#      time.sleep(0.1)
#      char_num = i//4
#      # \r表示每次都顶格打印
#      per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
#          if i == 100 else '\r%s%% : %s' % (i,'*'*char_num)
#      # 设置结束符为空，将所有内容打印在同一行，并且不缓存要打印内容，立即打印
#      print(per_str,end='', flush=True)


# def func(a):
#     return len(str(a)) >= 2

# li = [1,11,32,'12312','dadsad']
# # 找出可迭代对象中符合函数定义的筛选条件的值，并放在一个可迭代对象中
# res = filter(func,li)
# for i in res:
#     print(i)

# def myfunc(a):
#     if type(a) == int:
#         return a+1
#     elif type(a) == str:
#         return a+'1'
#
# res = map(myfunc,li)
# for i in res:
#     print(i)


# def myli():
#     return (lambda n:n*i for i in range(4))
#
# li = [ mylamb(2) for mylamb in myli()]
# print(li)

# tup = (('a','b'),('c','d'))
# li = list(zip(tup[0],tup[1]))
# print(li)
# dt_li = list(map(lambda item:{item[0]:item[1]},li))
# print(dt_li)

# dic={'k1':10,'k2':100,'k3':30}
# max_val_key = max(dic,key=lambda key:dic[key])
# print(max_val_key)
#
#
# sentence = 'select name,age where age>2'
# # select_item_li = sentence.strip().split(' ')[1].split(',')
# # condition = sentence.strip().split(' ')[-1]
# # print(select_item_li,condition)
#
# res_li = sentence.strip().split('select')[-1].strip().split('where')
# select_items_li = res_li[0].strip().split(',')
# condition_str = res_li[1].strip()
# print(select_items_li,condition_str)
# condition_dic = {}
# if '>' in condition_str:
#     condition_dic[condition_str.split('>')[0]] = condition_str.split('>')[1]
#
# print(condition_dic)

# def half_find(data_li,data):
#     '''
#     二分查找算法，实现在有序列表中查找某个数
#     :param data_li:
#     :param data:
#     :return:
#     '''
#     start = 0
#     end = len(data_li)-1
#     while start <= end:
#         mid = (start+end)//2
#         if data_li[mid] == data:
#             return mid,data_li[mid]
#         elif data_li[mid] > data:
#             end = mid-1
#         else:
#             start = mid+1
#     return
#
#
# data_li = list(range(1,100))
# res1 = half_find(data_li,57)
# print(res1)


# def myage(n):
#     '''
#     递归求某人的年纪
#     :param n:
#     :return:
#     '''
#     if n == 4:
#         return 40
#     elif 0 < n < 4:
#         return myage(n+1)+2
#
# print(myage(1))
#
#
# def re_half_find(li,data,start=0,end=None):
#     '''
#     使用递归实现二分查找
#     :param li:
#     :param data:
#     :param start:
#     :param end:
#     :return:
#     '''
#     end = len(li)-1 if end is None else end
#     mid = (start+end)//2
#     if start <= end:
#         if li[mid] == data:
#             return {'position':mid,'value':li[mid]}
#         elif li[mid] > data:
#             return re_half_find(li,data,start,mid-1)
#         else:
#             return re_half_find(li,data,mid+1,end)
#     else:
#         return "not find"
#
# if __name__ == '__main__':
#     data_li = list(range(1,100))
#     li = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
#     res1 = re_half_find(data_li,22)
#     print(res1)
#     res2 = re_half_find(li,67)
#     print(res2)
#
#
# def mymul(n):
#     '''
#     利用递归求某个数的阶乘
#     :param n:
#     :return:
#     '''
#     if n == 1:
#         return 1
#     else:
#         return n*mymul(n-1)
#
# print(mymul(4))


# 0 1 1 2 3 5 8 13 21
# def myfib(n):
#     '''
#     求取斐波那契数列第n个数的值，从1开始计数
#     :param n:
#     :return:
#     '''
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     if n == 3:
#         return 1
#     elif n > 3:
#         res = myfib(n-1) + myfib(n-2)
#         return res
#
# def buid_fib_li(n):
#     '''
#     求长度为n的斐波那契数列
#     :param n:
#     :return:
#     '''
#     fib_li = []
#     for i in range(1,n+1):
#         fib_li.append(myfib(i))
#     return fib_li
#
# print(myfib(9))
# print(buid_fib_li(9))

# import time
# print(time.mktime(time.localtime()))
# # 1550475011
# print(time.localtime(1650475010))

# # 基础队列的使用
# import queue
#
# q = queue.Queue()
# # 向队列中插入值
# q.put([1,2,3])
# q.put(5)
# q.put(6)
# # 从队列中获取不到数据时，程序会阻塞等待数据
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# # 获取队列的大小
# print(q.qsize())


# # 有序字典
# from collections import  OrderedDict
# # 创建字典时使用的另一个形式，元组第一个值是键，第二个是值
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od) # OrderedDict的Key是有序的
# print(od['a'])
# for k in od:
#     print(k)
#
# # 有默认值的字典
# from collections import defaultdict
# # 设置字典中不存在的键，在第一次创建时的默认值
# d = defaultdict(lambda : 5)
# print(d['k'])
# # 设置键的默认值为列表
# d1 = defaultdict(list)
# print(d1['a'])


# from collections import namedtuple
#
# Point = namedtuple('point',['x','y','z'])
# p1 = Point(1,2,3)
# p2 = Point(3,2,1)
# # 使用对象调用属性的方式调用元组中的值
# print(p1.x)
# print(p1.y)
# print(p1,p2)
# # 1
# # 2
# # point(x=1, y=2, z=3) point(x=3, y=2, z=1)

# import sys
#
# # 获取解释器运行的操作系统型号
# print(sys.platform)
# # 获取该操作系统的版本号
# print(sys.version)
# # 获取解释器进行路径查找时的路径列表
# print(sys.path)
# # win32
# # 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)]
# # ['C:\\Personal\\pycharm_projects\\......',]

import json

# test_dic = {'a':1,'b':2,'c':3,'d':'猪猪'}
# # 在内存中完成字典转字符串
# dic_str = json.dumps(test_dic)
# print(test_dic)
# print(dic_str)
# # 在内存中完成字符串转字典
# print(json.loads(dic_str))
#
# with open('json_test','w',encoding='utf-8') as f:
#     # 将转换后的字符串保存到文件中
#     json.dump(test_dic,f)
# with open('json_test') as f:
#     # 从文件中载入字符串，并反序列化
#     dd = json.load(f)
# print(dd)

# l = [{'k':'111'},{'k2':'111'},{'k3':'111'}]
# f = open('file','w')
#
# # 在内存中序列化字典，并逐行保存到文件中
# for dic in l:
#     str_dic = json.dumps(dic)
#     f.write(str_dic+'\n')
# f.close()
#
# # 读取文件内容到内存，并反序列化为字典
# f = open('file')
# l = []
# for line in f:
#     dic = json.loads(line.strip())
#     l.append(dic)
# f.close()
# print(l)

# import pickle
#
# l = [{'k':'111'},{'k2':'111'},{'k3':'111'}]
# # 将python的数据类型转换为bytes类型
# ls = pickle.dumps(l)
# print(ls)
# # 将bytes类型，转换为python的数据类型
# lr = pickle.loads(ls)
# print(lr)

# import time
# import pickle
#
# struct_time1  = time.localtime(1000000000)
# struct_time2  = time.localtime(2000000000)
#
# f = open('pickle_file','wb')
# # 将python的数据类型转换为bytes，并保存在文件中
# pickle.dump(struct_time1,f)
# pickle.dump(struct_time2,f)
# f.close()
#
# f = open('pickle_file','rb')
# # 从文件中读取bytes类型数据，转换为python的数据类型
# struct_time1 = pickle.load(f)
# struct_time2 = pickle.load(f)
# f.close()
#
# print(struct_time1.tm_year)
# print(struct_time2.tm_year)

# import shelve
# import datetime
#
# infor = {"name":"zzz","age":"100"}
# name = ["zhuzhu","jiji","dajiji"]
# t = datetime.datetime.now()
#
# # 使用shelve模块，将各种数据类型序列化后保存在文件中
# with shelve.open("test_shelve.txt") as shel_f:
#     shel_f["name"] = name
#     shel_f["infor"] = infor
#     shel_f["time"] = t

# import shelve
#
# f = shelve.open('shelve_file')
# # 直接对文件句柄操作，就可以存入数据
# f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}
# f.close()
# # 不设置writeback=True对文件句柄进行的修改操作，不会写入到序列化文件中
# f1 = shelve.open('shelve_file',writeback=True)
# print(f1['key'])
# f1['key']['new_value'] = 'this was not here before'
# print(f1['key'])
# f1.close()

# l = [{'k':'111'},{'k2':'111'},{'k3':'111'}]
# with shelve.open('shelve_file',writeback=False) as f:
#     f['l'] = l
#     print(f['l'])
#     # [{'k': '111'}, {'k2': '111'}, {'k3': '111'}]
#     f['l'].append({'k4':'123'})
#     print(f['l'])
#     # [{'k': '111'}, {'k2': '111'}, {'k3': '111'}]
#
# with shelve.open('shelve_file',writeback=True) as f:
#     f['l'] = l
#     print(f['l'])
#     # [{'k': '111'}, {'k2': '111'}, {'k3': '111'}]
#     f['l'].append({'k4':'123'})
#     print(f['l'])
#     # [{'k': '111'}, {'k2': '111'}, {'k3': '111'}, {'k4': '123'}]

# python2.7
# 新式类 继承object类的才是新式类 广度优先
# 经典类 如果你直接创建一个类在2.7中就是经典类 深度优先
# print(D.mro())
# D.mro()

# 单继承 ： 子类有的用子类 子类没有用父类
# 多继承中，我们子类的对象调用一个方法，默认是就近原则，找的顺序是什么？
# 经典类中 深度优先
# 新式类中 广度优先
# python2.7 新式类和经典类共存，新式类要继承object
# python3   只有新式类，默认继承object
# 经典类和新式类还有一个区别  mro方法只在新式类中存在
# super 只在python3中存在

# class A(object):
#     def func(self):
#         print('A') # 6
#
# class B(A):
#     def func(self):
#         super(B,self).func() # 4
#         print('B') # 8
#
# class C(A):
#     def func(self):
#         super(C,self).func() # 5
#         print('C') # 7
#
# class D(B,C):
#     def func(self):
#         # super的本质 ：不是单纯找本类的父类，
#         # 而是根据起始调用类的继承顺序来查找父类，
#         # 对于经典类，就是采用广度优先顺序来查找
#         super().func() # 3
#         print('D') # 9
#
# dobj = D() # 1
# dobj.func() # 2
# print(D.mro()) # 可以打印新式类的继承的顺序
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# class EnclosedClass(object):
#
#     __key = 'mysalt' # 定义类的私有属性
#
#     def __init__(self,name,passwd):
#         self.name = name
#         self.__passwd = passwd # 定义对象的私有属性
#
#     # 定义私有方法
#     def __get_finalpass(self):
#         return self.__passwd + EnclosedClass.__key
#
#     def get_passwd(self):
#         return self.__passwd
#
# myobj = EnclosedClass('zx','1234')
# print(EnclosedClass.__dict__)
# print(myobj.__dict__)
# # {'name': 'zx', '_EnclosedClass__passwd': '1234'}
# print(myobj._EnclosedClass__passwd)
# # 如果想要调用类的私有属性或函数，必须使用这样的格式
# print(myobj._EnclosedClass__get_finalpass())
# print(myobj.get_passwd())


# from abc import abstractmethod,ABCMeta
#
# class Payment(metaclass=ABCMeta):  # 元类 默认的元类 type
#     @abstractmethod
#     def pay(self,money):pass   # 没有实现这个方法
# # 规范 ：接口类或者抽象类都可以
# # 接口类 支持多继承，接口类中的所有的方法都必须不能实现 —— java
# # 抽象类 不支持多继承，抽象类中方法可以有一些代码的实现 —— java
#
# class Wechat(Payment):
#     def pay(self,money):
#         print('已经用微信支付了%s元'%money)
#
# class Alipay(Payment):
#     def pay(self,money):
#         print('已经用支付宝支付了%s元' % money)
#
# class Applepay(Payment):
#     def pay(self,money):
#         print('已经用applepay支付了%s元' % money)
#
# def pay(pay_obj,money):  # 统一支付入口
#     pay_obj.pay(money)
#
# apple_obj = Applepay()
# ali_obj = Alipay()
# pay(apple_obj,100)
# pay(ali_obj,100)


# class A:
#     def func(self):
#         print('in func')
#
# a = A()
# a.name = 'alex'
# a.age = 63
#
# # 反射对象的方法
# ret = getattr(a,'func') # 相当于a.func
# ret()
#
#
# class A:
#     price = 20
#     @classmethod
#     def func(cls):
#         print('in func')
#
# # 反射类的属性
# print(getattr(A,'price')) # 相当于A.price
#
# # 反射类的方法
# if hasattr(A,'func'):
#     getattr(A,'func')() # 相当于A.func()

# # 反射模块的属性
# import three_layer_table
#
# menu = {'1': {'12': {'113': {}}}, '2': {'22': {'223': {}}}, '3': {'33': {'333': {}}}}
# print(three_layer_table.MyThreeLayerTable(menu))
# # 通过反射获取模块的属性
# print(getattr(three_layer_table,'MyThreeLayerTable')(menu).show_table())

# 反射模块的方法
# getattr(my,'wahaha')()

# # 内置模块也能用
# import time
# print(getattr(time,'time')())
# print(getattr(time,'asctime')())

# def qqxing():
#     print('qqxing')
# year = 2018
# import sys
# # print(sys.modules[__name__].year)

# import sys
#
# year = '2020'
# def testfunc():
#     print('in testfunc')
#
# # 反射本模块中的变量
# print(getattr(sys.modules[__name__],'year'))
# # 反射自己模块中的函数
# getattr(sys.modules[__name__],'testfunc')()

# 变量名 = input('>>>')
# print(getattr(sys.modules[__name__],变量名))

# 要反射的函数有参数怎么办?
# print(time.strftime('%Y-%m-%d %H:%M:S'))
# print(getattr(time,'strftime')('%Y-%m-%d %H:%M:S'))

# 一个模块中的类能不能反射得到
# import my
# print(getattr(my,'C')())
# if hasattr(my,'name'):
#     getattr(my,'name')

# # 使用setattr，设置、修改属性值
# class A:
#     pass
# a = A()
# setattr(a,'name','nezha')
# setattr(A,'name','alex')
# print(A.name)
# print(a.name)
#
# # 使用delattr，删除属性
# delattr(a,'name')
# print(a.name)
# delattr(A,'name')
# print(a.name)

# try:
#     f = open('C:\\Personal\\pycharm_projects\\python_projects\others\\test_class.py','r',encoding='utf-8')
#     line = f.readline()
# # 测试try下面的语句，是不是有特定的错误，有就执行异常下面定义的语句
# except FileNotFoundError as fn_erro:
#     print(fn_erro)
# except Exception as e:
#     print(e)
# else: # try中的语句没有发生错误，才会执行的语句
#     f.close()
#     print(line)
# finally: # 不论try中的语句错误还是正确，都会执行
#     print('runs anyway')

# # 内置的打印显示方法
# # obj.__str__ :str(obj),直接打印 实际上都是走的__str__
# # obj.__repr__:repr(obj),实际上都是走的__repr__
# class Teacher:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#
#     def __str__(self):
#         # 打印一个对象时默认调用这个方法
#         return "Teacher's object :%s"%self.name
#
#     def __repr__(self):
#         # __repr__是__str__的备胎，但反过来则不行
#         return str(self.__dict__)
#
#     def func(self):
#         return 'wahaha'
#
# nezha = Teacher('fuckz',250)
# print(nezha)  # 打印一个对象的时候，就是调用a.__str__
# print(repr(nezha))
# print('>>> %r'%nezha)
# print(obj)/'%s'%obj/str(obj)的时候，
# 实际上是内部调用了obj.__str__方法，
# 如果有str方法，那么他必须返回一个字符串
# 如果没有__str__方法，会先找本类中的__repr__方法，
# 再看父类中是否有__str__方法，有就调用父类的__str__方法。
# repr(),只会找__repr__,如果没有找父类的，不会找本类的__str__方法。

# class Classes:
#     def __init__(self,name):
#         self.name = name
#         self.student = []
#
#     def __len__(self):
#         # 执行len()方法，其实就是在调用类的该内置函数
#         return len(self.student)
#
# py_s9= Classes('python_learning')
# py_s9.student.append('zx')
# py_s9.student.append('zzz')
# print(len(py_s9))


# # 类内置的析构函数，__del__
# class A:
#     def __del__(self):
#     # 析构函数: 在删除一个对象之前进行一些收尾工作
#         self.f.close()
# a = A()
# a.f = open('temp.txt')
# del a # del既执行了类中自定义的__del__方法，关闭文件，又调用默认的__del__方法删除了变量f
# 引用计数

# 在类的对象后面添加"()",就会执行类内置的__call__方法
# class A:
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self):
#         '''
#         打印这个对象中的所有属性
#         :return:
#         '''
#         for k in self.__dict__:
#             print(k,self.__dict__[k])
#
# a = A('haha')
# a()

# class Foo(object):
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __getitem__(self, item):
#         # 通过操作字典的方式,查看对象的属性
#         if hasattr(self,item):
#             return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         # 通过操作字典的方式,给对象的属性赋值
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         # 通过操作字典的方式,删除对象的某个属性
#         del self.__dict__[key]
#
# f = Foo('bigegg',38,'male')
# print(f['name'])
#
# f['hobby'] = 'fucking'
# print(f.hobby,f['hobby'])
#
# del f['hobby']
# print(f.__dict__)

# # 使用__new__方法,构建出self对象
# class A(object):
#
#     def __init__(self):
#         # 执行完__new__后,初始化构建出来的对象
#         self.x = 1
#         print('in init function')
#
#     def __new__(cls, *args, **kwargs):
#         # 使用object类的__new__方法,构建出self对象
#         print('in new function')
#         return object.__new__(cls)
#
# a = A()
# # in new function
# # in init function

# # 使用类的__new__方法,实现单实例类,
# # 就是此类只可以生成一个对象.
# class A(object):
#
#     __instance = False
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         # 如果此类已经生成了一个对象,返回生成的对象
#         if cls.__instance:
#             return cls.__instance
#
#         # 否则生成一个此类的新对象,并返回
#         cls.__instance = object.__new__(cls)
#         return cls.__instance
#
# tt1 = A('zx1',38)
# tt1.cloth = 'nike'
# tt2 = A('zx2',25)
# print(tt1)
# print(tt2)
# print(tt1.name)
# print(tt2.name)
# print(tt2.cloth)
# # <__main__.A object at 0x000002C7EBE6E240>
# # <__main__.A object at 0x000002C7EBE6E240>
# # zx2
# # zx2
# # nike

# class A(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def __eq__(self, other):
#         # 用"=="判断两个对象是否相等时,就会自动调用该方法
#         if self.__dict__ == other.__dict__:
#             return True
#         else:
#             return False
#
# ob1 = A('zx')
# ob2 = A('zx')
# print(ob1 == ob2)

# hash()   #__hash__
# class A(object):
#
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#
#     def __hash__(self):
#         # 调用hash方法,哈希对象时,就会调用类中定义的__hash__方法
#         return hash(self.name+self.sex)
#
# a = A('zx','male')
# b = A('ff','male')
# print(hash(a))
# print(hash(b))

# import json
# from collections import namedtuple
#
# Card = namedtuple('Card',['rank','suit'])
#
# class FranchDeck(object):
#     ranks = [str(n) for n in range(2,11)] + list('JQKA') # 生成牌的大小
#     suits = ['红心','方板','梅花','黑桃'] # 生成牌的花色
#
#     def __init__(self):
#         # 生成一副牌
#         self._cards = [
#             Card(rank,suit) for rank in FranchDeck.ranks
#                                         for suit in FranchDeck.suits]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, item):
#         return self._cards[item]
#
#     def __setitem__(self, key, value):
#         self._cards[key] = value
#
#     def __str__(self):
#         return json.dumps(self._cards,ensure_ascii=False)
#
# deck = FranchDeck()
# print(deck[10])
#
# from random import choice
# print(choice(deck))
#
# from random import shuffle
# shuffle(deck) # 会用到内置的__len__方法
# print(deck[10])
# print(deck)
# print(deck[:5])


# class A(object):
#
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def __eq__(self, other):
#         if self.name == other.name and self.sex == other.sex:
#             return True
#         return False
#
#     def __hash__(self):
#         return hash(self.name + self.sex)
#
# a = A('zx','female',38)
# b = A('zx','female',37)
# # 调用set计算两个对象的哈希值是否一样时,
# # 会调用类内置的__hash__和__eq__算法
# print(set((a,b)))

# import os
# import sys
#
# sys.path.append(os.path.dirname(os.getcwd()))
# # print(sys.path[-1])
# with open('C:\\Personal\\pycharm_projects\\python_projects\\others\\fortest','r',encoding='utf-8') as f:
#     # while True:
#     #     one_part = f.read(7)
#     #     print(one_part)
#     for line in f:
#         print(line)

# import configparser
# #
# # config = configparser.ConfigParser()
# #
# # # 设置一个大的section,下面的键值对定义在字典中
# # config["DEFAULT"] = {'ServerAliveInterval': '45',
# #                       'Compression': 'yes',
# #                      'CompressionLevel': '9',
# #                      'ForwardX11':'yes'
# #                      }
# # config['bitbucket.org'] = {'User':'hg'}
# # config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
# #
# # #将配置写入到文件中
# # with open('example.ini', 'w') as f:
# #    config.write(f)

# import configparser
#
# config = configparser.ConfigParser()
#
# config.read('example.ini')
# print(config.sections())
# # ['bitbucket.org', 'topsecret.server.com']
#
# print('bytebong.com' in config) # False
# print('bitbucket.org' in config) # True
#
# print(config['bitbucket.org']["user"])  # hg
# print(config['DEFAULT']['Compression']) # yes
# print(config['topsecret.server.com']['ForwardX11']) # no
#
# print(config['bitbucket.org'])
# # <Section: bitbucket.org>
#
# # 注意,有default会默认default的键
# for key in config['bitbucket.org']:
#     print(key)
#
# print(config.options('bitbucket.org'))
# # 同for循环,找到'bitbucket.org'下所有键
# print(config.items('bitbucket.org'))
# # 找到'bitbucket.org'下所有键值对
# print(config.get('DEFAULT','CompressionLevel'))
# get方法Section下的key对应的value

# 修改配置文件的内容
# import configparser
#
# config = configparser.ConfigParser()
# config.read('example.ini') # 读取配置文件
#
# config.add_section('yuan') # 增加一个section
# config.remove_section('bitbucket.org') # 删除一个section
#
# # 删除section中的一个配置项
# config.remove_option('topsecret.server.com',"forwardx11")
#
# # 为某个section设置新的键值对
# config.set('topsecret.server.com','k1','11111')
# config.set('yuan','k2','22222')
#
# # 将对配置文件的修改，保存到新文件
# f = open('new2.ini', "w")
# config.write(f)
# f.close()

# import logging
# class MyLogger(object):
#
#     def __init__(self):
#         # 第一步，创建一个logger
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#
#         # 第二步，创建一个handler，用于写入日志文件
#         logfile = settings.LOG_PATH
#         fh = logging.FileHandler(logfile, mode='a')
#         fh.setLevel(logging.DEBUG)
#
#         # 第三步，再创建一个handler，用于输出到控制台
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.WARNING)
#
#         # 第四步，定义handler的输出格式
#         formatter = logging.Formatter(settings.LOG_FORMAT)
#         fh.setFormatter(formatter)
#         ch.setFormatter(formatter)
#
#         # 第五步，将logger添加到handler里面
#         logger.addHandler(ch)
#         logger.addHandler(fh)
#
#         self.logger = logger
#
#     def get_logger(self):
#         return self.logger


# import socket
#
# cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# svr_addr = ('127.0.0.1',8080)
# conn,addr = cli.connect(svr_addr)
#
# conn.send(b'sadasdasd')

# # 发送断使用struct打包文件大小到要发送的报文中
# import struct
# import os
# import socket
#
# cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# svr_addr = ('127.0.0.1',8080)
# conn,addr = cli.connect(svr_addr)
#
# file_size = os.path.getsize('papapa.avi')
# dic = {'operate': 'upload', 'filename': 'papapa.avi', 'filesize': file_size}
# str_dic = json.dumps(dic).encode('utf-8')
# # 将字典的大小，转换成一个大小为四个字节的bytes类型
# ret = struct.pack('i', len(str_dic))
# # 将字典大小和字典打包发送
# conn.send(ret + str_dic)


# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',8080))
# sk.listen()
#
# conn,addr = sk.accept()
#
# # 首先接收四个字节大小的，描述要传递的描述报文大小的数据
# dic_len = conn.recv(4)
#
# # 通过unpact方法将bytes转换为数字
# dic_len = struct.unpack('i',dic_len)[0]
#
# # 根据字典的大小，精确的获取描述要传输的报文的属性
# content = conn.recv(dic_len).decode('utf-8')
# content_dic = json.loads(content)
#
# # 循环获取整个大文件的内容，同时写入本地文件
# if content_dic['operate'] == 'upload':
#     with open(content_dic['filename'],'wb') as f:
#         while content_dic['filesize']:
#             file = conn.recv(1024)
#             f.write(file)
#             content_dic['filesize'] -= len(file)
#
# conn.close()
# sk.close()

# 打印传输进度条
# import time
#
# def print_process(total_size,transfered_size):
#     i = int(transfered_size/total_size*100)
#     char_num = i//2
#     per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
#         if i == 100 else '\r%s%% : %s' % (i,'*'*char_num)
#     print(per_str,end='', flush=True)
#
# for t in range(1001):
#     time.sleep(0.01)
#     print_process(1000,t)