#!/usr/bin/python3.5

import os
def myos_test():
    ddd = os.getcwd()

    #os.chdir(r"C:\Personal") #修改当前工作目录
    #os.makedirs("%s/a/b"%(dd)) #递归的创建目录
    #os.removedirs("%s/a/b"%(dd)) #如果文件夹为空就递归删除目录
    # dd = os.stat("%s/new_f"%(dd)) #输出指定文件的属性元组
    # dd = dd.st_mode #调用文件属性元组中的相关属性
    # dd = os.name #显示操作系统的名称
    # dd = os.linesep
    # dd = os.sep
    # dd = os.pathsep
    # dd=os.curdir #返回当前目录.
    # os.pardir #显示父目录..
    #dd = os.system("ipconfig /all") #调用当前系统的命令,返回值是0或1...etc
    dd = os.path.getatime("%s/new_f"%(ddd)) #获取文件最近一次访问时间
    cc = os.path.getmtime("%s/new_f"%(ddd))
    tt = os.path.getctime("%s/new_f"%(ddd))


    print(dd,cc,tt)