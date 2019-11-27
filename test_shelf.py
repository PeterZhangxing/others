#!/usr/bin/python3.5
import shelve,datetime

infor = {"name":"zzz","age":"100"}
name = ["zhuzhu","jiji","dajiji"]
t = datetime.datetime.now()

with shelve.open("test_shelve.txt") as shel_f:
    shel_f["name"] = name
    shel_f["infor"] = infor
    shel_f["time"] = t
