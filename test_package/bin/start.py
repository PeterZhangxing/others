import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
from core.main import mymain,myexception

if __name__ == '__main__':
    # mymain(1,2,3,test='das')
    res = myexception(7)
    res1 = myexception(11)
    print(res)
    print(res1)