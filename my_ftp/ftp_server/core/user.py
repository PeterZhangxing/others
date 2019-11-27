import os
from conf import settings

class User:
    def __init__(self,name):
        self.name = name
        self.home = os.path.join(settings.home_path,name)
        self.cur_path = self.home # 用户登录时的默认目录
        self.disk_space = settings.space # 用户可以使用多大的磁盘空间
        self.file_size = 0 # 已经使用的磁盘空间