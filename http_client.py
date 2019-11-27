#!/usr/bin/python3.5

import requests,hashlib,time

def create_authkey_ctime(private_key):
    '''
    根据私有key和系统时间，生成发送给服务器端的认证密钥
    :return:
    '''
    current_time = time.time()
    key_ctime = "%s|%s"%(private_key,current_time)

    m = hashlib.md5()
    m.update(key_ctime.encode('utf-8'))
    authkey = m.hexdigest()

    authkey_ctime = "%s|%s"%(authkey,current_time)
    return authkey_ctime


def send_data(url,private_key,data):
    '''
    利用http协议将主机数据和密钥发送到服务器
    :param url:
    :param private_key:
    :param data:
    :return:
    '''
    try:
        # requests.get(url='http://127.0.0.1:8000/api/asset/?k1=123')
        # requests.get(url='http://127.0.0.1:8000/api/asset/',params={'k1':'v1','k2':'v2'})
        # requests.post(
        #     url='http://127.0.0.1:8000/api/asset/',
        #     params={'k1':'v1','k2':'v2'}, # GET形式传值
        #     data={'username':'1123','pwd': '666'}, # POST形式传值
        #     headers={'a':'123'} # 请求头数据
        # )
        response =requests.post(
            url=url,
            json=data, # 发送序列化后的数据给服务器端
            headers={'authkey': create_authkey_ctime(private_key)},
        )
        return response
    except Exception as e:
        return str(e)


if __name__ == '__main__':

    private_key = "x1i2j3i4n5g6p7i8n9g"
    url = 'http://127.0.0.1:8000/api/asset/'
    host_data = {
        'status': True,
        'data':{
            'hostname': 'c1.com',
            'disk': {'status':True,'data': 'xxx'},
            'mem': {'status':True,'data': 'xxx'},
            'nic': {'status':True,'data': 'xxx'},
        }
    }

    res = send_data(url,private_key,host_data)
    print(res)