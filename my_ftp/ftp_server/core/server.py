import json
import socketserver
from core import views
from conf import settings

class MyFTPServer(socketserver.BaseRequestHandler):
    logined_lst = {} # 已登录列表

    def my_recv(self):    # 派生方法
        msg = self.request.recv(1024)
        msg = msg.decode(settings.code)
        msg = json.loads(msg)
        return msg

    def my_send(self,msg):
        msg = json.dumps(msg).encode(settings.code)
        self.request.send(msg)

    def handle(self):
        while True:
            msg = self.my_recv()
            op_str = msg['operation']
            if op_str == 'login' or op_str == 'register':
                if hasattr(views,op_str):
                    func = getattr(views,op_str)
                    ret,pickle_path = func(msg)
                if ret:
                    MyFTPServer.logined_lst[self.client_address] = pickle_path
                    self.my_send(ret)
            elif hasattr(views,op_str) and self.client_address in MyFTPServer.logined_lst:
                func = getattr(views, op_str)
                ret = func(msg, self.request)
                self.my_send(ret)
            else:
                self.my_send(False)