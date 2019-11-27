from core import login

def mymain(*args,**kwargs):
    print(args,kwargs)
    login.mylogin()

def myexception(a):
    try:
        if int(a) > 9:
            raise ValueError
    except Exception as e:
        return 'value over 9'
    else:
        return a
    finally:
        print('final part of test exception')
