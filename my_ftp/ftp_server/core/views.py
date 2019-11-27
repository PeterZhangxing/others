import os
import pickle
from core.user import User
from conf import settings

def login(msg):
    # 登录 用户名 密码
    # 获取到pickle_path
    print(msg)
    # return True,pickle_path

def register(msg):
    # username , password
    # 把用户名密码 写进 userinfo文件里，记录用户名
    user_obj = User(msg['username'])  # 记录用户的信息在内存里
    pickle_path = os.path.join(settings.pickle_path,msg['username'])
    with open(pickle_path,'wb') as f:
        pickle.dump(user_obj,f)
    os.mkdir(user_obj.home) # 创建一个属于这个用户的家目录
    with open(settings.user_info,'a') as f:
        f.write('%s|%s|%s\n'%(msg['username'],msg['password'],pickle_path))
    return True,pickle_path

def upload(msg,request):
    # 如果这个过程 涉及到上传下载，sk
    print(msg)

def download(msg):
    print(msg)