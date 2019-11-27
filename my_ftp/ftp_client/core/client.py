from core.auth_client import Auth

def main():
    auth_obj = None
    start_l = [('登录', 'login'), ('注册', 'register'), ('退出', 'exit')]
    for index,item in enumerate(start_l,1):
        print(index,item[0])
    while True:
        try:
            num = int(input('>>>').strip())
            func_str = start_l[num-1][1]
        except:
            print('请输入正确的选项号!')
        if hasattr(Auth,func_str):
            auth_obj = Auth()
            func = getattr(auth_obj,func_str)
            ret = func()
            if ret:
                break
        elif auth_obj:
            auth_obj.socket.sk.close()
            exit()
        else:
            exit()