#!/usr/bin/python3.5
import time,shelve

with shelve.open("test_shelve.txt") as f:
    da = f.get("name")
    db = f.get("time")
    dc = f.get("infor")

dd = [da,db,dc]
print(dd)
for i in dd:
    if i == da:
        print(i[1])
    elif i == dc:
        print(i["name"])
    else:
        print(i)

