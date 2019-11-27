#!/usr/bin/python3.5
#通过事先定义好元祖和字典的方式把元祖和字典传递给函数
def test_func1(a,b):
     print(a[0])
     print(b['America'])

a = ("apple","banaba","tulip","pineapple","celery","pear")
b = {
    'America':"by working really hard you can get whatever you want!",
    'NewZaeland':"you will be surrounded by nature!",
    'china':"million years of life!"
}

test_func1(a,b)

#通过在调用函数的参数中直接使用实参和位置参数来传递元祖和字典给函数
# def test_func1(*args,**kwargs):
#     print(args[1])
#     print(kwargs['America'])

# test_func1("apple","banaba","tulip","pineapple","celery","pear",America="by working really hard you can get whatever you want!",
#     NewZaeland="you will be surrounded by nature!",
#     china="million years of life!")