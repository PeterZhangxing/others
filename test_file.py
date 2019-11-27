#!/usr/bin/python3.5

f = open("fortest","w",encoding="utf-8")
for i in range(20):
    f.write("this is my first line!\n")
f.close()

f = open("fortest","r",encoding="utf-8")
#print(f.readlines()) #读取文件内容并转换为一个列表
#print(f.readline(10)) #一次读取一行数据，并可以指定读取多少个字符
#print(f.tell()) #告诉你目前光标在哪个位置
#print(f.seek(0)) #移动光标回到你指定的位置
#print(f.readline(8))
'''
for index,item in enumerate(f.readlines()):
    print(index,item)
    print("______divided line_______")
'''
#使用遍历列表的方式遍历文件内容，因为会将整个文件存储在内存中，所以并不推荐使用
'''
for line in f:
    print(line.strip())
'''
#最为常用的遍历文件每一行的方法，不会把整个文件读取到内存中，推荐使用

f.close()