#!/usr/bin/python3.5

import sys

old_file = input("please input the full name of the file you want to change its content: ")
f = open(old_file,"r",encoding="utf-8")
f_new = open("new_f","w",encoding="utf8")

find_word = input("enter the word you want to replace: ")
repl_word = input("enter the word you want to input: ")

def change_content(findx,repx):
    for line in f:
        if findx in line:
            line = line.replace(findx,repx)
        f_new.write(line)
    f.close()
    f_new.close()

change_content(find_word,repl_word)
print("the content has been changed,and we have put it in a new file called new_f!")
