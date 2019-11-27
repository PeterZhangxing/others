#!/usr/bin/python3.5
code = '''
def fib(n):
    a,b,i = 0,1,0
    while i<n:
        yield b
        a,b = b,a+b
        i +=1

tt = fib(5)

while True:
    try:
        x = next(tt)
        print(x)
    except StopIteration as e:
        print("general return value: ",e.value)
        break
'''

#exec(code) #可以把文本格式的代码转换为可执行代码

cal = lambda n:3 if n<4 else n
print(cal(-1))