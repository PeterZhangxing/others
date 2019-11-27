#!/usr/bin/python3.5

import random

def check_random(n):
    if n.isdigit():
        n = int(n)
    else:
        return "Invalid Input,we can only accept one number as parameter!Please retry!"
    checkcode = ''
    for i in range(n):
        current_random = random.randrange(0,n)
        if i == current_random:
            tmp = chr(random.randint(65,90))
        else:
            tmp = random.randrange(1,10)
        checkcode += str(tmp)
    return checkcode

b_flag = True
while b_flag:
    n = input("Please input how many numbers of checkcode member do you want: ").strip()
    if n == "quit" or n == "exit" or n == "q":
        b_flag = False
        print("Exit the programme...")
    else:
        tt = check_random(n)
        print(tt)