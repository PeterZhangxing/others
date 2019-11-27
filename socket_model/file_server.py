#!/usr/bin/python3.7

import socket
import os
import hashlib

ip_port = ('192.168.31.168',8019)
buffer = 2048
holding_num = 5

tcp_ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_ser.bind(ip_port)
tcp_ser.listen(holding_num)
print("started tcp server")


def send_data(tcp_conn,data):
    data_size = len(data)
    if data_size == 0:
        return False
    tcp_conn.send(str(data_size).encode('utf-8'))
    echo_info = tcp_conn.recv(1024)
    if echo_info:
        tcp_conn.send(data)
        return True
    return False


def recv_data(tcp_conn):
    data_size = int(tcp_conn.recv(1024).decode('utf-8'))
    tcp_conn.send('OK'.encode('utf-8'))
    rec_size = 0
    data = b''
    while data_size - rec_size > 1024:
        data += tcp_conn.recv(1024)
        rec_size += 1024
    else:
        data += tcp_conn.recv(data_size - rec_size)
    return data


def recv_save_file(tcp_conn,filename):

    hobj = hashlib.md5()
    file_size = int(tcp_conn.recv(1024).decode('utf-8'))
    print(file_size)
    tcp_conn.send("OK".encode('utf-8'))
    with open(filename,'wb') as f:
        rec_file_size = 0
        while file_size - rec_file_size > 2048:
            file_content = tcp_conn.recv(2048)
            hobj.update(file_content)
            f.write(file_content)
            rec_file_size += len(file_content)

        file_content = tcp_conn.recv(file_size - rec_file_size)

        hobj.update(file_content)
        f.write(file_content)
        print(os.path.getsize(file_name))

    with open(filename+'.md5','w',encoding='utf-8') as mf:
        mf.write(recv_data(tcp_conn).decode('utf-8'))
        mf.write('\n')
        mf.write(str(hobj.hexdigest()))
    return True


while True:
    conn, addr = tcp_ser.accept()
    print("recieved new connection request")

    file_name = recv_data(conn).decode('utf-8')
    print(file_name)

    trans_file_res = recv_save_file(conn, file_name)
    if trans_file_res:
        choice = input("sucessed!continue to receive file?(y/n):")
        if choice.strip().lower() == "y":
            continue
        else:
            break

conn.close()
tcp_ser.close()