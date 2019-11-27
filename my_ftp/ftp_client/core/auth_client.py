from core.socket_client import MySocketClient

class Auth(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = object.__new__(cls)
            obj.socket = MySocketClient()
            obj.username = None
            cls.__instance = obj
        return cls.__instance

    def login(self):
        username = input('username : ').strip()
        password = input('password : ').strip()
        if username and password:
            self.socket.mysend({'username':username,
                                'password':password,
                                'operation':'login'})
        ret = self.socket.sk.recv(1024)

    def register(self):
        username = input('username : ').strip()
        password1 = input('password : ').strip()
        password2 = input('password_ensure : ').strip()
        if username and password1 and password1 == password2:
            self.socket.mysend({'username': username,
                                'password': password1,
                                'operation': 'register'})
        ret = self.socket.sk.recv(1024)