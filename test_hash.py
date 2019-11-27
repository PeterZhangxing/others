#!/usr/bin/python3.5

import hashlib

m = hashlib.sha512() #创建一个hash对象，可以指定加密算法
m.update("it is a test".encode(encoding="utf_8")) #把需要hash的字符传递给该对象
print(m.hexdigest()) #用16进制方式进行加密