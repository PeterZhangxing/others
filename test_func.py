#!/usr/bin/python3.5

def test(x,y):
    z = x**y
    return z

def use_test(x,y):
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        result = test(x,y)
        print("the result of x calculating y would be: %s" %(result))
    else:
        print("invalid input,please retry it!")

while True:
    t = input('please input t: ')
    if t == "exit" or t == "quit" or t == "q":
        print("you are exiting........")
        break
    else:
        x = input('please input x: ')
        y = input('please input y: ')
        use_test(x=x,y=y)