#################### 多线程实现并发访问url地址 ####################

# import threading
# import requests
#
# url_li = [
#     'http://www.baidu.com/',
#     'https://www.cnblogs.com/',
#     'https://www.cnblogs.com/news/',
#     'https://cn.bing.com/',
#     'https://stackoverflow.com/',
# ]
#
# def access_url(urladd):
#     res = requests.get(urladd)
#     print(res.status_code)
#
# for url in url_li:
#     t = threading.Thread(target=access_url,args=(url,))
#     t.start()

#################### 携程实现并发访问url地址 ####################

# from gevent import monkey; monkey.patch_all()
# import gevent
# import requests
#
# url_li = [
#     'http://www.baidu.com/',
#     'https://www.cnblogs.com/',
#     'https://www.cnblogs.com/news/',
#     'https://cn.bing.com/',
#     'https://stackoverflow.com/',
# ]
#
# def access_url(urladd):
#     res = requests.get(urladd)
#     print(res.status_code)
#
# spawn_li = []
#
# for url in url_li:
#     spawn_li.append(gevent.spawn(access_url, url))
#
# gevent.joinall(spawn_li)

#################### twisted实现并发访问url地址 ####################

# from twisted.web.client import getPage,defer
# from twisted.internet import reactor
#
# def stop_loop(arg):
#     reactor.stop()
#
# def get_response(contents):
#     print(contents)
#
# url_list = [
#     'http://www.baidu.com/',
#     'https://www.cnblogs.com/',
#     'https://www.cnblogs.com/news/',
#     'https://cn.bing.com/',
#     'https://stackoverflow.com/',
# ]
#
# deferred_list = []
#
# for url in url_list:
#     deferred = getPage(bytes(url, encoding='utf8'))
#     deferred.addCallback(get_response)
#     deferred_list.append(deferred)
#
# dlist = defer.DeferredList(deferred_list)
# dlist.addBoth(stop_loop)
#
# reactor.run()

#################### 使用IO多路复用实现并发访问url地址 ####################

import socket
import select

class MyMulIO(object):

    def __init__(self):
        self.socket_list = []
        self.conn_list = []
        self.conn_func_dict = {}

    def add_request(self,url_func):
        conn = socket.socket()
        conn.setblocking(False)

        try:
            conn.connect((url_func[0],80))
        except BlockingIOError:
            pass

        self.conn_func_dict[conn] = url_func[1]

        self.socket_list.append(conn)
        self.conn_list.append(conn)

    def run(self):
        while True:
            r,w,e = select.select(self.socket_list,self.conn_list,[],0.05)

            for sock in w:
                sock.send(b'GET / http1.1\r\nhost:xxxx.com\r\n\r\n')
                self.conn_list.remove(sock)

            for sock in r:
                data = sock.recv(8096)
                func = self.conn_func_dict[sock]

                func(data)

                sock.close()

                self.socket_list.remove(sock)

            if not self.socket_list:
                break


if __name__ == '__main__':

    def callback1(data):
        print('下载完成1', data)

    def callback2(data):
        print('下载完成2', data)

    urls = [
        ('www.baidu.com', callback1),
        ('www.cnblogs.com', callback1),
        ('www.pythonav.com', callback2),
        ('www.bing.com', callback2),
        ('www.stackoverflow.com', callback2),
    ]

    myio = MyMulIO()
    for url in urls:
        myio.add_request(url)

    myio.run()