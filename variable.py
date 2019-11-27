#!/usr/bin/pyhton3.5
#在函数中将默认的局部变量改为全局变量
name = 'obama'
age = '45'
occupation = 'wreched'
def test_func():
    global name
    name = 'triump'
    age= '71'
    occupation = 'presendent of us'
    print(name,age,occupation)
test_func()
print(name,age,occupation)

a = [[1,2,3],[4,5,6],[7,8,9]]
print(a.index([1,2,3]))
a.remove(a[1])
a.reverse()
print(a)