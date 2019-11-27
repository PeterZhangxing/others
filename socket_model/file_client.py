#!/usr/bin/python3.7

import socket
import os
import hashlib
import time


ip_port = ('10.1.1.128',8019)
# buffer = 2048

tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_client.connect(ip_port)


def print_process(total_size,transfered_size):
    i = int(transfered_size/total_size*100)
    char_num = i//2
    per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
        if i == 100 else '\r%s%% : %s' % (i,'*'*char_num)
    print(per_str,end='', flush=True)


def send_data(data):
    data_size = len(data)
    if data_size == 0:
        return False
    tcp_client.send(str(data_size).encode('utf-8'))
    echo_info = tcp_client.recv(1024)
    if echo_info:
        tcp_client.send(data)
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


def load_send_file(filename,buffer=2048):
    # send file name
    send_data(filename.encode('utf-8'))

    # get file size
    file_size = os.path.getsize(filename)
    print(file_size)

    # send file size before sending file contents
    tcp_client.send(str(file_size).encode('utf-8'))
    echo_info = tcp_client.recv(1024)

    # load and send file as byte style
    if echo_info:
        my_sha = hashlib.md5()
        with open(filename,'rb') as f:
            read_size = 0
            start_time = time.time()
            while True:
                if file_size-read_size > buffer:
                    f_content = f.read(buffer)
                    my_sha.update(f_content)
                    tcp_client.send(f_content)
                    read_size = f.tell()
                    print_process(file_size,read_size)
                else:
                    buffer = file_size-read_size
                    f_content = f.read(buffer)
                    my_sha.update(f_content)
                    tcp_client.send(f_content)
                    read_size = f.tell()
                    print_process(file_size, read_size)
                    print('finishing transfer file %s'%filename)
                    break

        # send hashed value of file
        hash_res = my_sha.hexdigest()
        end_time = time.time()
        run_time = end_time - start_time
        tran_speed = round(file_size/(1024*1024)/run_time,2)
        # print(run_time)
        print("upload speed %sM/s"%tran_speed)
        # print(hash_res)
        return send_data(hash_res.encode('utf-8'))
    else:
        return False


def juge_choice():
    u_choice = input('do you want to transfer file agian?(y/n)').strip()
    if u_choice.lower() == 'y':
        return True
    return False


if __name__ == '__main__':

    while True:
        file_path = input('full Path of your file>>>').strip()
        if os.path.isfile(file_path):
            load_send_file(file_path)
            if juge_choice():
                continue
            else:
                break
        elif os.path.isdir(file_path):
            print('%s is a directory,we cannot transfer!'%file_path)
            continue
        else:
            print('%s is not exist,try agian.')
            continue

    tcp_client.close()