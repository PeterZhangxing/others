#!/usr/bin/python3.5

import time
def timer(func):
    def deco(*args,**kwargs):
        start_t = time.time()
        func(*args,**kwargs)
        stop_t = time.time()
        print("The runing time of this function is about %s" %(start_t-stop_t))
    return deco

@timer
def test1(*args,**kwargs):
    print(*args,**kwargs)
    time.sleep(3)
    print("In the test1 now!")

test1(1,2,3)