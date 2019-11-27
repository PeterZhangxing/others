#!/usr/bin/python3.5

import sys,time
while True:
    counts = input("please input the number of # you want to see: ")
    if counts.isdigit():
        counts = int(counts)
        for i in range(counts):
            sys.stdout.write("#")
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n")
    elif counts == "exit" or counts == "q":
        break
print("you have quit the programme")


